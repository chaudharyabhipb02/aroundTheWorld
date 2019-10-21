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

class flight_avail(models.Model):
    From =models.CharField(max_length=225)
    to = models.CharField(max_length=225)
    arrival = models.CharField(max_length=225)
    departure = models.CharField(max_length=225)
    date = models.CharField(max_length=225)
    category = models.CharField(max_length=225)
    trip_type = models.CharField(max_length=225)
    charges = models.CharField(max_length=225)
class flight_book(models.Model):
    From =models.CharField(max_length=225)
    to = models.CharField(max_length=225)
    arrival = models.CharField(max_length=225)
    departure = models.CharField(max_length=225)
    date = models.CharField(max_length=225)

    category = models.CharField(max_length=225)
    trip_type = models.CharField(max_length=225)
    charges = models.CharField(max_length=225)
    uid = models.ForeignKey(tb_register, on_delete=models.PROTECT)
class flight_payment(models.Model):
    fid = models.ForeignKey(flight_book, on_delete=models.PROTECT)
    costing = models.CharField(max_length=225)
    payment_mode = models.CharField(max_length=225)
    booking_date = models.CharField(max_length=225)
    uid = models.ForeignKey(tb_register, on_delete=models.PROTECT)