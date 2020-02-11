from django.db import models

# Create your models here.


class ToDo(models.Model):
    content = models.CharField(max_length=100, null=False)
    date_added = models.DateField()

    def __str__(self):
        return self.content
