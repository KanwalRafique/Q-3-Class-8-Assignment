# app.py

from flask import Flask, render_template, request, redirect, url_for
from library import Library, Book, EBook

app = Flask(__name__)
lib = Library()

@app.route('/')
def index():
    books = lib.get_books()
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        book_type = request.form['type']
        title = request.form['title']
        author = request.form['author']

        if book_type == 'ebook':
            file_format = request.form['format']
            lib.add_book(EBook(title, author, file_format))
        else:
            lib.add_book(Book(title, author))

        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/borrow/<title>')
def borrow_book(title):
    book = lib.find_book(title)
    if book:
        book.borrow()
    return redirect(url_for('index'))

@app.route('/return/<title>')
def return_book(title):
    book = lib.find_book(title)
    if book:
        book.return_book()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
