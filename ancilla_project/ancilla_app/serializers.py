from rest_framework import serializers

from .models import StaffUser, Patron, Book, Checkout, Hold


class StaffUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StaffUser
        fields = ["url", "username", "email", "first_name", "last_name"]


class PatronSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patron
        fields = ["url", "name", "address", "phone", "expire_date"]


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ["url", "title", "author", "genre"]


class CheckoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Checkout
        fields = ["url", "patron", "book", "checkout_date", "due_date"]


class HoldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hold
        fields = ["url", "patron", "book", "hold_date"]
