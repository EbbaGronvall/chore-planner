from django.urls import path
from households import views

urlpatterns = [
    path('households/', views.HouseholdList.as_view()),
    path('households/<slug:slug>/', views.HouseholdDetail.as_view()),
]