# **Books Parser**

**Books Parser** — это веб-приложение на Django, которое позволяет искать книги по названию, цене и рейтингу, парсить информацию с сайтов и фильтровать результаты.

## **Функционал**

- Поиск книг по названию, цене и рейтингу
- Фильтрация результатов
- Парсинг данных с внешних сайтов
- Сохранение результатов в базе данных
- Управление книгами через Django Admin

---

## **Стек технологий**

- **Backend**: Python 3.12, Django  
- **Database**: PostgreSQL  
- **Frontend**: HTML  
- **Парсинг**: BeautifulSoup, requests  
- **Контейнеризация**: Docker, Docker Compose  

---

## **Как развернуть проект**

### **1. Клонирование репозитория**

```sh
git clone https://github.com/dvokivon/books_parser.git
cd books_parser
```
### **2. Запуск проекта в Docker**

```sh
docker-compose up -d --build
```

### **3. Выполнить миграции и создать суперпользователя**
```sh
docker-compose exec web python manage.py migrate
```

### **4. Открыть в браузере**

Frontend (пользовательский интерфейс): http://localhost:8000
