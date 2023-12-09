from django.http.response import HttpResponse

from rest_framework import permissions, viewsets

from .models import StaffUser, Patron, Book, Checkout, Hold
from .serializers import (
    StaffUserSerializer,
    PatronSerializer,
    BookSerializer,
    CheckoutSerializer,
    HoldSerializer,
)

# Create your views here.


def index(request):
    return HttpResponse("Hello World!")


class StaffUserSet(viewsets.ModelViewSet):
    """
    API endpoint that allows staff users to be viewed or edited.
    """

    queryset = StaffUser.objects.filter(is_active=True).order_by("-date_joined")
    serializer_class = StaffUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class PatronSet(viewsets.ModelViewSet):
    """
    API endpoint that allows patrons to be viewed and edited.
    """

    queryset = Patron.objects.all().order_by("name")
    serializer_class = PatronSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed and edited.
    """

    queryset = Book.objects.all().order_by("title")
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class CheckoutSet(viewsets.ModelViewSet):
    """
    API endpoint that allows checkout records to be viewed and edited.
    """

    queryset = Checkout.objects.all().order_by("-checkout_date")
    serializer_class = CheckoutSerializer
    permission_classes = [permissions.IsAuthenticated]


class HoldSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hold records to be viewed and edited.
    """

    queryset = Hold.objects.all().order_by("-hold_date")
    serializer_class = HoldSerializer
    permission_classes = [permissions.IsAuthenticated]
