from django.contrib import admin

from myapp.models import tb_register
from myapp.models import feedback

admin.site.register(tb_register)
admin.site.register(feedback)

# Register your models here.
