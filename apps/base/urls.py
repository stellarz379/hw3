from django.urls import path

from apps.base.views import about,contact, news, time

urlpatterns = [
   path('about/', about, name="about"),
   path('contact/', contact, name="contact"),
   path('news/', news, name="news"),
   path('time/', time, name="time"),
]