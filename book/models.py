from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    body = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=7)
    cover_picture = models.ImageField(upload_to='books/')
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title

class BookQuantity(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)