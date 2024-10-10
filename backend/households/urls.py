from django.urls import path
from .views import HouseholdList

urlpatterns = [
    path('households/', HouseholdList.as_view())
]