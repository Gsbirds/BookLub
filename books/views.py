from django.shortcuts import render, redirect
from .models import File
from .forms import FileForm
import fitz
from collections import Counter

# def dummy_create_index(received_file):
#     pass

    ## check if file is a pdf

    ## check if file has been received before (compare file hashes)

    ## if the file has not been received then read all text contents into an array

    ## array_of_words_from_pdf_filtered = [word for word in array_of_words_from_pdf if word not in STOP_WORDS_ARRAY]

    ## counter = Counter(array_of_words_from_pdf_filtered)

    ## most_common_words = counter.most_common(100)

    ## store most_common_words in ArrayField model that ties the list of words to an uploaded file

# def search_dummy(term):
#     ## return a list of all files that contain the search term(s) with links to interact with them


def search_results(request):
    posts= File.objects.all()
    search_post = request.GET.get('search')
    if search_post:
        posts = File.objects.filter (name__icontains=search_post)
        
    else:
        posts = File.objects.all()
    return render(request, "books/list.html", {"posts":posts})   
    
def showfile(request):
    form= FileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        uploads=form.save(False)
        uploads.author=request.user
        uploads.save()
        return redirect("search")
    context= { 
              'form': form
              }
      
    return render(request, 'books/upload.html', context)

def redirect_to_page(request):
    return redirect("search")