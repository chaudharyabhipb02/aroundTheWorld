from django.db import models


class tb_register(models.Model):

    name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    contact = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    gender = models.CharField(max_length=225)

    def __str__(self):
        return self.name
