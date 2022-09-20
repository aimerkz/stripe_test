from django.urls import path
from api.views import (
    get_info_item, get_buy_id, CancelView, SuccessView, get_buy_order)


app_name = 'api'

urlpatterns = [
    path('item/<int:id>', get_info_item, name='info_item'),
    path('buy/<int:id>', get_buy_id, name='buy'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('buy_order/<int:id>', get_buy_order, name='buy_order'),
]
