from django.shortcuts import render, redirect, get_object_or_404
from .models import File, CommonWords
from .forms import FileForm
import fitz
from collections import Counter
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from collections import Counter
import fitz
# models.py

def pdf_reader(request):
    pdfs = File.objects.all()
    words=CommonWords.objects.all()
    return render(request, 'books/pdf_reader.html', {'pdfs':pdfs, 'words':words})

def search_words(request):
    posts1= File.objects.all()
    search_word = request.GET.get('search')
    if search_word:
        posts1 = CommonWords.objects.filter (word__icontains=search_word)
        print(posts1)
    else:
        posts1 = File.objects.all()
    return render(request, "books/list.html", {"posts1":posts1})  

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
                file_instance.save()
                file_instance.author = request.user
                file_instance.save()

                # Extract text from the PDF
                pdf_path = file_instance.filepath.path  # Use the path of the saved file
                pdf_text = ""
                pdf_document = fitz.open(pdf_path)
                for page_num in range(pdf_document.page_count):
                    page = pdf_document.load_page(page_num)
                    pdf_text += page.get_text()

                # Process text and get top 100 words
                words = pdf_text.lower().split()
                word_count = Counter(words)
                top_100_words = word_count.most_common(100)

                # Save the top 100 words to the CommonWords model
                for word, word_count in top_100_words:
                    CommonWords.objects.create(pdf=file_instance, word=word)

        return render(request, 'books/upload.html', {"form": form})

    else:
        form = FileForm()

    return render(request, 'books/upload.html', {"form": form})

def redirect_to_page(request):
    return redirect("search")
