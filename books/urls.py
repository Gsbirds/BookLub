from django.urls import path
from .views import search_results, showfile, word_search


urlpatterns = [
    path("",search_results, name="search"),
    path("upload/",showfile, name="upload"),
     path("word_search/",word_search, name="word_search"),
]