from django.db import models

class users(models.Model):
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.login

