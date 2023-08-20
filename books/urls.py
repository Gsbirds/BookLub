from django.urls import path
from .views import search_results, showfile, pdf_reader, search_words


urlpatterns = [
    path("",search_results, name="search"),
    path("search_words",search_words, name="search_words"),
    path("upload/",showfile, name="upload"),
    path("pdf_reader",pdf_reader, name="pdf_reader"),

]