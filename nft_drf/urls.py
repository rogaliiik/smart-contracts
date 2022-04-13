from django.urls import path, include
from .views import TokenAPICreate, TokenAPIList


urlpatterns = [
    path('tokens/create/', TokenAPICreate.as_view()),
    path('tokens/list/', TokenAPIList.as_view()),
    # path('tokens/total_supply/', pass)
]