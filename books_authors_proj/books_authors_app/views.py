from django.shortcuts import render,redirect,HttpResponse
from .models import *


#books
def books(request):

    all_books = get_all_books()

    context = {
        "books": all_books
    }

    return render(request, "books.html", context)


def create_book_view(request):

    if request.method == "POST":

        title = request.POST["title"]
        desc = request.POST["desc"]

        create_book(title, desc)

        return redirect("/books")

    return redirect("/books")


def show_book(request, book_id):

    book = get_book(book_id)

    authors = get_authors_not_associated_with_book(book)

    context = {
        "book": book,
        "authors": authors
    }

    return render(request, "show_book.html", context)


def add_author_to_book_view(request, book_id):

    if request.method == "POST":

        book = get_book(book_id)

        author_id = request.POST["author_id"]

        author = get_author(author_id)

        add_author_to_book(book, author)

    return redirect(f"/books/{book_id}")


#authors
def authors(request):

    all_authors = get_all_authors()

    context = {
        "authors": all_authors
    }

    return render(request, "authors.html", context)


def create_author_view(request):

    if request.method == "POST":

        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        notes = request.POST["notes"]

        create_author(
            firstname,
            lastname,
            notes
        )

        return redirect("/authors")

    return redirect("/authors")


def show_author(request, author_id):

    author = get_author(author_id)

    books = get_books_not_associated_with_author(author)

    context = {
        "author": author,
        "books": books
    }

    return render(request, "show_author.html", context)


def add_book_to_author_view(request, author_id):

    if request.method == "POST":

        author = get_author(author_id)

        book_id = request.POST["book_id"]

        book = get_book(book_id)

        add_book_to_author(author, book)

    return redirect(f"/authors/{author_id}")