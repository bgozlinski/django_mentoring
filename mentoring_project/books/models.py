from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Book(models.Model):
    class StatusChoices(models.TextChoices):
        AVAILABLE = 'available', 'Available'
        ARCHIVED = 'archived', 'Archived'
        BORROWED = 'borrowed', 'Borrowed'

    author = models.ForeignKey('books.Author', related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    status = models.CharField(
        max_length=32,
        choices=StatusChoices.choices,
        default=StatusChoices.AVAILABLE,
    )

    def __str__(self):
        return f"{self.title} by {self.author} - {self.status}"