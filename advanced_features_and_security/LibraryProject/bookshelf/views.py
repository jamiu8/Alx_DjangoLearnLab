from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookForm
from django.db.models import Q
from .models import User
from .forms import SearchForm

# Create your views here.

@permission_required('yourapp.can_view', raise_exception=True)
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

@permission_required('yourapp.can_create', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

@permission_required('yourapp.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})

@permission_required('yourapp.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')

def search_user(request):
    form = SearchForm(request.GET)
    users = []
    if form.is_valid():
        query = form.cleaned_data['query']
        users = User.objects.filter(Q(username__icontains=query) | Q(email__icontains=query))
    return render(request, 'search.html', {'form': form, 'users': users})