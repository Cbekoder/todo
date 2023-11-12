from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateField()
    text = models.CharField(max_length=50)
    condition = models.CharField(max_length=20)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title