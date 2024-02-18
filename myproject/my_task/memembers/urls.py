from django.urls import path
from . import views


urlpatterns =[
    path('',views.Fibonnacciview ,name ='Fibonnacciview'),
    path('generatefibonnacci/',views.generatefibonnacci,name='generatefibonnacci'),
]
   
    