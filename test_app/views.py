from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Order
from .serializers import OrderSerializer


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class OrderListView(ListAPIView):
    # queryset = Order.objects.all()
    queryset = Order.objects.select_related("customer", "merchant").prefetch_related(
        "orderitem_set__product"
    )
    serializer_class = OrderSerializer
    pagination_class = CustomPagination
