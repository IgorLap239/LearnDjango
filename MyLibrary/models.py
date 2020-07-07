from django.db import models

class authors(models.Model):
    surname = models.TextField()
    name = models.TextField()
    birthday = models.DateField()

    def __str__(self):
        return self.surname

class my_library(models.Model):
    book_name = models.TextField()
    author = models.ForeignKey(
        authors,
        on_delete=models.CASCADE,
    )
    year = models.DateField()
    pages = models.IntegerField()
