from django.urls import path
from .views import TokenAPITotalSupply, TokenAPICreate, TokenViewSet


urlpatterns = [
    path('tokens/create/', TokenAPICreate.as_view()),
    path('tokens/list/', TokenViewSet.as_view({'get': 'list'})),
    path('tokens/list/<int:pk>', TokenViewSet.as_view({'get': 'retrieve'})),
    path('tokens/total_supply/', TokenAPITotalSupply.as_view())
]