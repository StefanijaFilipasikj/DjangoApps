from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# Create your views here.


def books(request):
    if request.method == 'POST':
        form_data = BookForm(request.POST, files=request.FILES)
        if form_data.is_valid():
            form = form_data.save(commit=False)
            form.user = request.user
            form.image = form_data.cleaned_data['image']
            form.save()
            return redirect('books')

    form = BookForm()
    books = Book.objects.all()
    return render(request, 'books.html', {"books": books, "form": form})


def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'book_details.html', {'book': book})


def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('books')
