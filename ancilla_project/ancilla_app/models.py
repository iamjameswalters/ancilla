from datetime import date, timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models

GENRE_CHOICES = (
    ("M", "Mystery"),
    ("B", "Biography/Autobiography"),
    ("F", "Fantasy"),
    ("H", "Historical Fiction"),
    ("P", "Poetry"),
    ("R", "Romance"),
    ("S", "Science Fiction"),
    ("T", "Thriller/Suspense"),
)


def two_years_from_now():
    two_years = timedelta(days=730)
    today = date.today()
    return today + two_years


def three_weeks_from_now():
    three_weeks = timedelta(days=21)
    today = date.today()
    return today + three_weeks


# Create your models here.


class StaffUser(AbstractUser):
    def __str__(self):
        return self.username


class Patron(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    expire_date = models.DateField(default=two_years_from_now, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=80)
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES)


class Checkout(models.Model):
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(default=three_weeks_from_now, blank=True)


class Hold(models.Model):
    patron = models.ForeignKey(Patron, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    hold_date = models.DateField(auto_now_add=True)
