from django.conf.urls import url
from. import views
urlpatterns=[url(r'pro',views.pro,name='pro'),
             url(r'about',views.about,name='about'),
             url(r'destination', views.destination, name='destination'),
             url(r'contacts', views.contacts, name='contacts'),
             url(r'tour', views.tour, name='tour'),
             url(r'home', views.home, name='home'),
             url(r'register', views.register, name='register'),
             url(r'login', views.login, name='login'),
             url(r'amritsar', views.amritsar, name='asr'),
             url(r'display', views.display_feedback, name='display'),
             url(r'logout', views.delete_session, name='logout'),
             url(r'com', views.common, name='com'),
             url('book', views.book, name='book'),
             url('sff', views.search, name='sff'),
             url('bbbb', views.f_book, name='bbbb'),





            ]
