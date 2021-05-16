from django.urls import path

from .views import hello_world
from .views import pharmacies_view, pharmacies_detail, pharmacy_create
from .views import medicines_detail, medicines_view, medicine_create
from .views import distribution_detail, distribution_view, distribution_create


urlpatterns = [
    path('', hello_world),

    path('pharmacies/', pharmacies_view, name="pharmacies-list"),
    path("pharmacies/<int:pk>/", pharmacies_detail, name="pharmacy-detail"),
    path("pharmacies/create", pharmacy_create, name="pharmacy-create"),

    path("medicines/", medicines_view, name="medicines-list"),
    path("medicines/<int:pk>/", medicines_detail, name="medicine-detail"),
    path("medicines/create", medicine_create, name="medicine-create"),

    path("distribution/", distribution_view, name="distribution-list"),
    path("distribution/<int:pk>/", distribution_detail, name="distribution-detail"),
    path("distribution/create", distribution_create, name="distribution-create"),
]

