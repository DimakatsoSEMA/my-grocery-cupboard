from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Example extra field
    role = models.CharField(
        max_length=20,
        choices=[
            ('admin', 'Admin'),
            ('member', 'Member'),
        ],
        default='member'
    )

    def __str__(self):
        return self.username

