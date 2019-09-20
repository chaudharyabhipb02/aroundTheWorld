from django.conf.urls.static import static

from jpro import settings
from jpro.settings import MEDIA_ROOT,MEDIA_URL
from django.conf.urls import url
from. import views
urlpatterns=[url(r'^$',views.welcome_page,name='index'),
             url("form",views.registrations,name='myapp1'),
             url("myapp2",views.new_page,name='myapp'),
             url("login",views.login,name='myapp'),
             url("thanks/", views.template_thanks, name='myapp'),
             url("emp", views.empl, name='myapp'),
             url("page", views.model_form_upload, name='load'),
             url('display', views.Display_Image, name="display")


            ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
