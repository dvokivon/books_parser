import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from .models import Book

BASE_URL = "https://books.toscrape.com/catalogue/"


def get_soup(url):
    """Получение HTML страницы"""
    print(f"Запрашиваем URL: {url}") 
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Ошибка {response.status_code}: сайт недоступен")
    return BeautifulSoup(response.text, "html.parser")


def parse_book_page(book_url):
    """Парсит страницу книги и извлекает данные"""
    soup = get_soup(book_url)

    title = soup.find("h1").text.strip()
    price = soup.find("p",class_="price_color").text.strip().replace("£", "")[1::]
    print(price)
    availability = "In stock" in soup.find("p", class_="instock").text
    rating_class = soup.find("p", class_="star-rating")["class"]
    rating = rating_to_int(rating_class[1])

    return {
        "title": title,
        "price": float(price),
        "availability": availability,
        "rating": rating
    }


def rating_to_int(rating_str):
    """Конвертирует текстовый рейтинг в число"""
    ratings = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    return ratings.get(rating_str, None)


def parse_books_from_category(category_url):
    """Парсит книги из категории"""
    category_full_url = urljoin(BASE_URL, category_url)  # Полный URL категории
    soup = get_soup(category_full_url)
    books = soup.select("h3 > a")

    for book in books:
        relative_url = book["href"]
        print(BASE_URL)
        print(relative_url)
        book_url = urljoin(category_full_url, relative_url)
        print(book_url)
        data = parse_book_page(book_url)

        Book.objects.update_or_create(
            title=data["title"],
            defaults={
                "price": data["price"],
                "availability": data["availability"],
                "rating": data["rating"]
            }
        )
    print(f"Категория {category_url} загружена.")