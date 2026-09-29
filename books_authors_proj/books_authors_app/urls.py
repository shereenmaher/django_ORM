from django.urls import path
from . import views

urlpatterns = [

    # Books
    path("books", views.books),
    path("books/create", views.create_book_view),
    path("books/<int:book_id>", views.show_book),
    path("books/<int:book_id>/add-author",views.add_author_to_book_view
    ),

    # Authors
    path("authors", views.authors),
    path("authors/create", views.create_author_view),
    path("authors/<int:author_id>", views.show_author),
    path("authors/<int:author_id>/add-book",views.add_book_to_author_view
    ),
]