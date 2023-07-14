from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contatc"),
    path('table',views.table,name="table"),
    path('image',views.image,name="image"),
    path('form',views.form,name="form"),
    path('delete/<int:s_id>',views.delete,name="delete")
    
]