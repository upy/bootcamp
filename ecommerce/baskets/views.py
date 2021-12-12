# from rest_framework import viewsets
#
# from core.mixins import DetailedViewSetMixin
# from baskets.filters import BasketFilter
# from baskets.filters import BasketItemFilter
# from baskets.models import BasketItem, Basket
# from products.serializers import ProductSerializer, CategorySerializer, \
#     ProductDetailedSerializer
#
#
# class ProductViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filterset_class = ProductFilter
#     serializer_action_classes = {
#         "detailed_list": ProductDetailedSerializer,
#         "detailed": ProductDetailedSerializer,
#     }
#
#
# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
