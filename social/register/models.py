from django.db import models

# Create your models here.


class User(models.Model):
    stat = [(1, 'Active'), (2, 'Inactive')]
    first_name = models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=False, blank=False, max_length=100)
    user_name = models.CharField(primary_key=True, blank=False, null=False, max_length=100)
    password = models.CharField(blank=False, null=False, max_length=100)
    email = models.EmailField(blank=False, null=False, max_length=100)
    status = models.CharField(default=1, choices=stat, max_length=1)

    def __str__(self):
        return self.user_name
