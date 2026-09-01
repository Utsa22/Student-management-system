from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='students'
    )

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    roll = models.PositiveIntegerField()

    department = models.CharField(
        max_length=100
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):

        return self.name