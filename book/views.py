from django.shortcuts import render
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView )
from book.models import Book


class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'book_list'


class BookDetailView(DetailView):
    model = Book
    fields = '__all__'
    template_name = 'book/book_detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    template_name = 'book/book_create.html'
    fields = '__all__'


class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'book/book_update.html'



class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book/book_delete.html'