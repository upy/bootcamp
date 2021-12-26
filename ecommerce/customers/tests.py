from django.test import TestCase
from rest_framework.test import APIRequestFactory

from customers.factories import AddressFactory, CityFactory, CustomerFactory
from customers.models import Address, City, Country
from customers.serializers import AddressSerializer


class AddressSerializerTestCase(TestCase):
    def setUp(self):
        self.customer = CustomerFactory()
        self.serializer = AddressSerializer
        self.factory = APIRequestFactory()
        self.city = CityFactory()

    def test_new_address_default_false(self):
        request = self.factory.post("/api/addresses")
        request.user = self.customer
        data = {
            "name": "test address",
            "full_name": "mehmet caner",
            "line_1": "Fenerbahce Mh. No:1",
            "line_2": "",
            "phone": "+901234567890",
            "district": "Kadikoy",
            "zipcode": "34000",
            "city": self.city.id,
            "is_default": False,
        }
        serializer = self.serializer(data=data, context={"request": request})
        self.assertTrue(serializer.is_valid(raise_exception=True))
        self.assertEqual(Address.objects.count(), 0)
        serializer.save()
        self.assertEqual(Address.objects.count(), 1)

    def test_update_address_with_put(self):
        address_true = AddressFactory(customer=self.customer)
        address_true.is_default = True
        address_true.save()

        address_false = AddressFactory(customer=self.customer)

        request = self.factory.put(f"/api/addresses/{address_false.id}/")
        request.user = self.customer
        data = {
            "name": address_false.name,
            "full_name": address_false.full_name,
            "line_1": address_false.line_1,
            "line_2": address_false.line_2,
            "phone": address_false.phone,
            "district": address_false.district,
            "zipcode": address_false.zipcode,
            "city": address_false.city.id,
            "is_default": True,
        }
        serializer = self.serializer(
            data=data, context={"request": request}, instance=address_false
        )
        self.assertTrue(serializer.is_valid(raise_exception=True))
        serializer.save()
        self.assertTrue(Address.objects.get(id=address_false.id).is_default)
        self.assertFalse(Address.objects.get(id=address_true.id).is_default)
