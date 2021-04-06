from django.shortcuts import render
from .forms import BookCreateForm,BookUpdateForm
from .models import Book
from django.shortcuts import redirect

# Create your views here.
def home(request):
    books=Book.objects.all()
    context={}
    context["books"]=books
    return render(request,"book/index.html",context)


def book_create(request):
    form=BookCreateForm()
    context={}
    context["form"]=form
    template_name="book/bookcreate.html"
    books=Book.objects.all()
    context["books"]=books
    if request.method=="POST":
        form=BookCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print("inside")
            return redirect("create")
        else:
            context["form"]=form
            return render(request, template_name, context)
    return render(request,template_name,context)

#book/view/1
  #get return boom with corresponding id

def view_book(request,id):
    book=Book.objects.get(id=id)
    context={}
    context["book"]=book
    return render(request,"book/bookview.html",context)

#book/update/1
  #get return boom with corresponding id
  #post update book

def update_book(request,id):
    book = Book.objects.get(id=id)
    form=BookUpdateForm(instance=book)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BookUpdateForm(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            return redirect("create")
        else:
            form = BookUpdateForm(request.POST, instance=book)
            context["form"] = form
            return render(request, "book/bookedit.html", context)
    return render(request,"book/bookedit.html",context)


#book/delete/1
  #get delete book with id

def delete_book(request,id):
    book = Book.objects.get(id=id).delete()
    return redirect("create")
