from . import views
from django.urls import path

urlpatterns = [
   
    path('',views.hfun),
    path('About',views.abfun)
]
