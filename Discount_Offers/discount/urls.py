from django.urls import path
from .views import discount_form_view, success_view, download_db_as_excel  # Correct import

urlpatterns = [
    path('', discount_form_view, name='discount_form'),
    path('success/', success_view, name='success'),
    path('download-excel/', download_db_as_excel, name='download_excel'),  # Use correct view
]
