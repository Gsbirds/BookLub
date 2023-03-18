from django.shortcuts import render, redirect, get_object_or_404
from .models import File, Common_words
from .forms import FileForm
import fitz
from collections import Counter
from django.http import HttpResponse, HttpResponseRedirect

def word_get(request, id):
    if request.method=="POST":
        file=get_object_or_404(File,id=id)
        file=get_object_or_404(Common_words,id=id)
        doc = fitz.open(file)
        text = ""
        for page in doc:
            text.append(page.get_text())
        print(text)

        occurence_count = Counter(text)
    # text_count=occurence_count.most_common(1)[0][0]
        occurence_count.sort
        for i in range(len(occurence_count)):
            if i<=7:
                Common_words.words=occurence_count[i]

    return (request, 'books/upload.html')

def word_search(request):
    common= Common_words.objects.all()
    search_post = request.GET.get('search_words')
    if search_post:
        common = Common_words.objects.filter (words__icontains=search_post)
        
    else:
        common = File.objects.all()
    return render(request, "books/list.html", {"common":common})   
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
        posts = File.objects.filter (filepath__icontains=search_post)
        
    else:
        posts = File.objects.all()
    return render(request, "books/list.html", {"posts":posts})   
    
def showfile(request):   
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        files = request.FILES.getlist('filepath')
        if form.is_valid():
            for f in files:
                file_instance = File(filepath=f)
                file_instance.save(False)
                file_instance.author=request.user
                file_instance.save()
                # return redirect("search")
    else:
         form = FileForm()

    return render(request, 'books/upload.html', {"form": form})

def redirect_to_page(request):
    return redirect("search")

