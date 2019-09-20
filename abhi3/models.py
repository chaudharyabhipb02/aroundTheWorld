from django.db import models

# Create your models here.
from django.db import models

class web1(models.Model):
    news_head = models.CharField(max_length=225)
    news_web = models.CharField(max_length=225)
    news_img = models.ImageField()
    date = models.DateField()
class NEWS(models.Model):
    TITLE = models.CharField(max_length=225)
    authors = models.CharField(max_length=225)
    publisher = models.ForeignKey(web1,on_delete=models.PROTECT)
    PUBLICATION_date=models.DateField()
class tb_registrations(models.Model):

    name = models.CharField(max_length=225)
    email = models.CharField(max_length=225)
    contact = models.CharField(max_length=225)
    address = models.CharField(max_length=225)
    password = models.CharField(max_length=225)
    gender = models.CharField(max_length=225)


class employee(models.Model):
    e_id = models.CharField(max_length=225)
    e_salary = models.CharField(max_length=225)
    e_exp = models.CharField(max_length=225)
    e_profile = models.CharField(max_length=225)
    e_detail = models.ForeignKey(tb_registrations,on_delete=models.PROTECT)

class DOCUMENT(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='document/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description+" "+self.document

