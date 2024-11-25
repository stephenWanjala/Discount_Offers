from django.urls import path
from .views import discount_form_view, success_view

urlpatterns = [
    path('', discount_form_view, name='discount_form'),
    path('success/<str:message>/', success_view, name='success'),  # Add success view
]
