from django.db import models
class tb_register(models.Model):

    name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    contact = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    gender = models.CharField(max_length=225)
class feedback(models.Model):
    name = models.CharField(max_length=225)
    uid = models.ForeignKey(tb_register,on_delete=models.PROTECT)
    message = models.CharField(max_length=225)
    image = models.FileField(upload_to='img_doc/', blank=True, null=True)