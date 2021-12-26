import factory
from factory.django import DjangoModelFactory

from customers.models import Address, City, Country, Customer


class CustomerFactory(DjangoModelFactory):
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    is_active = True
    is_superuser = False
    is_staff = False

    class Meta:
        model = Customer


class CountryFactory(DjangoModelFactory):
    name = factory.Faker("name")

    class Meta:
        model = Country


class CityFactory(DjangoModelFactory):
    name = factory.Faker("name")
    country = factory.SubFactory(CountryFactory)

    class Meta:
        model = City


class AddressFactory(DjangoModelFactory):
    name = factory.Faker("text", max_nb_chars=20)
    customer = factory.SubFactory(CustomerFactory)
    full_name = factory.Faker("text", max_nb_chars=20)
    line_1 = factory.Faker("text", max_nb_chars=20)
    phone = factory.Sequence(lambda n: "+901234567890")
    district = factory.Faker("text", max_nb_chars=20)
    zipcode = factory.Faker("text", max_nb_chars=20)
    city = factory.SubFactory(CityFactory)

    class Meta:
        model = Address
