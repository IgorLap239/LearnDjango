from django.shortcuts import render

from MyLibrary.forms import libraryForm, authorsForm
from MyLibrary.models import authors, my_library


# Create your views here.

def library(request):
    if request.method == 'POST':
        # form = libraryForm(request.POST)
        # if form.is_valid():
        new_book = my_library()

        new_book.book_name = request.POST.get('book_name')
        author_id = request.POST.get('author')
        author = authors.objects.get(id=author_id)
        new_book.author = author
        new_book.year = request.POST.get('year')
        new_book.pages = request.POST.get('pages')
        new_book.save()

    all_books = my_library.objects.all()
    library_form = libraryForm()
    context = {'all_books': all_books, 'library_form': library_form}
    return render(request, 'MyLibrary/library.html', context)


def books_authors(request):
    if request.method == 'POST':
        # тут мы создаем новую книгу:
        new_author = authors()

        new_author.surname = request.POST.get('surname')

        new_author.name = request.POST.get('name')

        new_author.birthday = request.POST.get('birthday')

        new_author.save()

    all_authors = authors.objects.all()
    authors_form = authorsForm()
    context = {'all_authors': all_authors, 'authors_form': authors_form}
    return render(request, 'MyLibrary/authors.html', context)
