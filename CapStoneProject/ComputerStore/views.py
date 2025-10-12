from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# auth imports
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import Role # built in User model
from django.contrib.auth.mixins import LoginRequiredMixin

def homepage (request):
    return render(request,'homepage.html')

def login(request):
    return render(request,'login.html')

def support(request):
    return render(request,'support.html')

class AuthorListView(LoginRequiredMixin, ListView):
    model = Users
    template_name='authors/all-authors.html'
    context_object_name = 'all_authors'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/author-details.html'
    context_object_name = 'author'
    pk_url_kwarg = 'id'


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model=Author
    form_class = AuthorForm
    template_name = 'authors/author-form.html'
    success_url= reverse_lazy('author_list')


class AuthorUpdateView(UpdateView):
    model=Author
    form_class = AuthorForm
    template_name = 'authors/author-form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('author_list')

class AuthorDeleteView(DeleteView):
    model = Author
    success_url = reverse_lazy('author_list')


class SignUpView(CreateView):
    model = User
    form_class= UserCreationForm
    success_url = '/auth/login'
    template_name = 'registration/sign-up.html'

# CRUD for the books with author

class BookListView(ListView):
    model=Book
    template_name='books/book-list.html'
    context_object_name = 'books'

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book-list.html',{'books':books})


class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book-form.html'
    form_class = BookForm
    success_url=reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/book-form.html'
    form_class = BookForm
    success_url = reverse_lazy('book_list')
