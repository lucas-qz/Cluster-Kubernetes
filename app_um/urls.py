from django.urls import path
from . import views as vw
urlpatterns = [
    path('',vw.galeryview,name='galeryview'),  
]