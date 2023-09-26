from .views import *
from django.urls import path

urlpatterns = [
   path('', home,name="home"),
   path('send', send,name="send"),
   path('done', done,name="send"),
]
