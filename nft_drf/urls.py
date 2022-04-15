from django.urls import path
from .views import TokenAPITotalSupply, TokenAPICreate, TokenAPIList


urlpatterns = [
    path('tokens/create/', TokenAPICreate.as_view()),
    path('tokens/list/', TokenAPIList.as_view()),
    path('tokens/total_supply/', TokenAPITotalSupply.as_view())
]