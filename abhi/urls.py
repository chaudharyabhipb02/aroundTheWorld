from django.conf.urls import url
from. import views
urlpatterns=[url(r'^$',views.hello,name='index'),]
urlpatterns=[url(r'^$',views.template_home,name='index'),]
urlpatterns=[url(r'^$',views.order_demo,name='index'),]
