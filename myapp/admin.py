from django.contrib import admin
from myapp.models import feedback
from myapp.models import tb_register
from myapp.models import flight_avail
from myapp.models import flight_book
from myapp.models import flight_payment


admin.site.register(tb_register)
admin.site.register(feedback)
admin.site.register(flight_avail)
admin.site.register(flight_book)
admin.site.register(flight_payment)


# Register your models here.
