from django.shortcuts import render, redirect
from .models import File
from .forms import FileForm
from django.http import HttpResponse


def search_results(request):
    posts= File.objects.all()
    search_post = request.GET.get('search')
    if search_post:
        posts = File.objects.filter (name__icontains=search_post)
        print(posts)
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

