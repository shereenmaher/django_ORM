from django.db import models

#from books_authors_app.models import *
class Book(models.Model):
    title=models.CharField(max_length=255)
    desc=models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="authors")
    notes=models.CharField(max_length=255,default="old Author")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#Books

def get_all_books():
    return Book.objects.all()


def create_book(title, desc):
    return Book.objects.create(
        title=title,
        desc=desc
    )


def get_book(book_id):
    return Book.objects.get(id=book_id)


def get_books_not_associated_with_author(author):
    return Book.objects.exclude(authors=author)


#authors
def get_all_authors():
    return Author.objects.all()


def create_author(firstname, lastname, notes):
    return Author.objects.create(
        firstname=firstname,
        lastname=lastname,
        notes=notes
    )


def get_author(author_id):
    return Author.objects.get(id=author_id)


def get_authors_not_associated_with_book(book):
    return Author.objects.exclude(books=book)


#many to many functions
def add_author_to_book(book, author):
    book.authors.add(author)


def add_book_to_author(author, book):
    author.books.add(book)