from django.conf.urls import url
from. import views
urlpatterns=[url(r'pro',views.pro,name='pro'),
             url(r'about',views.about,name='about'),
             url(r'destination', views.destination, name='destination'),

             url(r'tour', views.tour, name='tour'),
             url(r'home', views.home, name='home'),
             url(r'register', views.register, name='register'),
             url(r'login', views.login, name='login'),
             url(r'sss', views.sis, name='sis'),
             url(r'flight', views.flight, name='flight'),
             url(r'feedbacks', views.feedbacks, name='feed'),
             url(r'display', views.display_feedback, name='display'),
             url(r'logout', views.delete_session, name='logout'),
             url(r'com', views.common, name='com')




            ]
