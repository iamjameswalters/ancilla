from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("staff", views.StaffUserSet)
router.register("patrons", views.PatronSet)
router.register("books", views.BookSet)
router.register("checkouts", views.CheckoutSet)
router.register("hold", views.HoldSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

urlpatterns += router.urls
