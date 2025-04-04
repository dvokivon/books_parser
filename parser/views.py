from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ParserForm
from .models import Book
from .utils import parse_books_from_category

CATEGORIES = {
    "Travel": "category/books/travel_2/index.html",
    "Mystery": "category/books/mystery_3/index.html",
    "Historical Fiction": "category/books/historical-fiction_4/index.html",
    "Sequential Art": "category/books/sequential-art_5/index.html",
    "Classics": "category/books/classics_6/index.html",
    "Philosophy": "category/books/philosophy_7/index.html",
    "Romance": "category/books/romance_8/index.html",
    "Womens Fiction": "category/books/womens-fiction_9/index.html",
    "Fiction": "category/books/fiction_10/index.html",
    "Childrens": "category/books/childrens_11/index.html",
    "Religion": "category/books/religion_12/index.html",
    "Nonfiction": "category/books/nonfiction_13/index.html",
    "Music": "category/books/music_14/index.html",
    "Default": "category/books/default_15/index.html",
    "Science Fiction": "category/books/science-fiction_16/index.html",
    "Sports and Games": "category/books/sports-and-games_17/index.html",
    "Fantasy": "category/books/fantasy_19/index.html",
    "New Adult": "category/books/new-adult_20/index.html",
    "Young Adult": "category/books/young-adult_21/index.html",
    "Science": "category/books/science_22/index.html",
    "Poetry": "category/books/poetry_23/index.html",
    "Paranormal": "category/books/paranormal_24/index.html",
    "Art": "category/books/art_25/index.html",
    "Psychology": "category/books/psychology_26/index.html",
    "Autobiography": "category/books/autobiography_27/index.html",
    "Parenting": "category/books/parenting_28/index.html",
    "Adult Fiction": "category/books/adult-fiction_29/index.html",
    "Humor": "category/books/humor_30/index.html",
    "Horror": "category/books/horror_31/index.html",
    "History": "category/books/history_32/index.html",
    "Food and Drink": "category/books/food-and-drink_33/index.html",
    "Christian Fiction": "category/books/christian-fiction_34/index.html",
    "Business": "category/books/business_35/index.html",
    "Biography": "category/books/biography_36/index.html",
    "Thriller": "category/books/thriller_37/index.html",
    "Contemporary": "category/books/contemporary_38/index.html",
    "Spirituality": "category/books/spirituality_39/index.html",
    "Academic": "category/books/academic_40/index.html",
    "Self Help": "category/books/self-help_41/index.html",
    "Historical": "category/books/historical_42/index.html",
    "Christian": "category/books/christian_43/index.html",
    "Suspense": "category/books/suspense_44/index.html",
    "Short Stories": "category/books/short-stories_45/index.html",
    "Novels": "category/books/novels_46/index.html",
    "Health": "category/books/health_47/index.html",
    "Politics": "category/books/politics_48/index.html",
    "Cultural": "category/books/cultural_49/index.html",
    "Erotica": "category/books/erotica_50/index.html",
    "Crime": "category/books/crime_51/index.html",
    "All": "all",
}


def index(request):
    """Главная страница с парсером и поиском"""
    if request.method == "POST":
        form = ParserForm(request.POST)
        if form.is_valid():
            category = form.cleaned_data["category"]
            if category == "All":
                for url in CATEGORIES.values():
                    if url != "all":
                        parse_books_from_category(url)
            else:
                parse_books_from_category(CATEGORIES[category])

            messages.success(
                request,
                f"Категория '{category}' успешно спарсена!"
                )
            return redirect("index")

    else:
        form = ParserForm()

    query = request.GET.get("query", "")
    price = request.GET.get("price", "")
    rating = request.GET.get("rating", "")

    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query)

    if price:
        try:
            books = books.filter(price__lte=float(price))
        except ValueError:
            pass

    if rating:
        try:
            rating = int(rating)
            if 0 <= rating <= 5:
                books = books.filter(rating=rating)
        except ValueError:
            pass

    return render(request, "parser/index.html", {"form": form, "books": books, "query": query, "price": price})
