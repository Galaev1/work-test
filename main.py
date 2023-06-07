# Импортируем необходимые библиотеки


from flask import Flask, render_template, request
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем приложение Flask
app = Flask(__name__)

# Создаем подключение к базе данных
engine = create_engine('sqlite:///books_and_movies.db')
Base = declarative_base()

# Определяем модели для таблиц книг и фильмов
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    genre = Column(String)

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)
    genre = Column(String)

# Создаем таблицы в базе данных
Base.metadata.create_all(engine)

# Создаем сессию для работы с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# Определяем маршруты для главной страницы, страниц добавления книг и фильмов и страницы вывода всех книг и фильмов
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        # Получаем данные из формы
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        # Создаем объект книги и добавляем его в базу данных
        book = Book(title=title, author=author, genre=genre)
        session.add(book)
        session.commit()
        # Возвращаем сообщение об успешном добавлении
        return f'Книга {title} успешно добавлена!'
    else:
        # Возвращаем форму для добавления книги
        return render_template('add_book.html')

@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        # Получаем данные из формы
        title = request.form['title']
        director = request.form['director']
        genre = request.form['genre']
        # Создаем объект фильма и добавляем его в базу данных
        movie = Movie(title=title, director=director, genre=genre)
        session.add(movie)
        session.commit()
        # Возвращаем сообщение об успешном добавлении
        return f'Фильм {title} успешно добавлен!'
    else:
        # Возвращаем форму для добавления фильма
        return render_template('add_movie.html')

@app.route('/show_all')
def show_all():
    # Получаем все книги и фильмы из базы данных
    books = session.query(Book).all()
    movies = session.query(Movie).all()
    # Возвращаем страницу с выводом всех книг и фильмов
    return render_template('show_all.html', books=books, movies=movies)

# Запускаем приложение
if __name__ == '__main__':
    app.run(debug=True)
