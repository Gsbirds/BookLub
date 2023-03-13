from django.urls import path
from .views import search_results, showfile


urlpatterns = [
    path("",search_results, name="search"),
    path("upload/",showfile, name="upload"),
]