from django.urls import path

from . import views

urlpatterns = [path("", views.main, name="main"),
               path("vehicles/", views.vehicles, name="vehicles"),
               path("payment/", views.payment, name="payment"),
]