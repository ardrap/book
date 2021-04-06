from django.shortcuts import render
from django.views.generic import ListView
from.models import Book
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import BookCreateForm
from django.urls import reverse_lazy

# Create your view
#List view
#Detail view
#Update view
#Delete view

class BookList(ListView):
   model=Book
   context_object_name="books"
   template_name="cbvbook/books.html"

class BookView(DetailView):
   model=Book
   context_object_name = "book"
   template_name = "cbvbook/bookdetail.html"

class BookCreate(CreateView):
   model=Book
   form_class=BookCreateForm
   template_name = "cbvbook/bookcreate.html"
   success_url = reverse_lazy('list')


class BookUpdate(UpdateView):
   model=Book
   form_class = BookCreateForm
   template_name = "cbvbook/bookcreate.html"
   success_url = reverse_lazy('list')

class BookDelete(DeleteView):
   model = Book
   success_url = reverse_lazy('list')