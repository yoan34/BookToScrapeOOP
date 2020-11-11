'''
Fichier principal ou l'on importe les composants pour
faire fonctionner le script.

'''

from components.BeautifulRequest import BeautifulRequest
from components.Book import Book
from components.Category import Category
from components.FileManager import FileManager


# Le point de départ du scraper.
BASE_URL = 'http://books.toscrape.com/'

request = BeautifulRequest(BASE_URL)
categories_urls = request.get_urls()

# Pour chaque URL de catégorie, on crée une instance
# de 'Category' qui initialise les URLS des pages
# existante et un fichier CSV.
for category_url in categories_urls:
    html = request.get_html(category_url)
    category = Category(category_url, html)
    fileManager = FileManager(category.name)

    # Affiche à la console des informations sur la catégorie.
    print(category, flush=True)

    # A chaque page on récupère le code HTML et on
    # scan la page pour ajouter les URLS de tous les
    # livres dans le dictionnaire 'category.pages'.
    for n, page_url in enumerate(category.pages):
        html = request.get_html(page_url)
        category.get_books(page_url, html)

        # Affiche à la console une distinction entre les pages.
        print('\n{}page {}:'.format(' '*3, n+1), flush=True)

        # On parcourt l'URL des livres pour récupérer le code
        # HTML et par la suite ses informations et on les
        # ajoute dans le fichier CSV.
        for (m, book_url) in enumerate(category.pages[page_url]):
            html = request.get_html(book_url)
            book = Book(book_url, html)

            # Affiche à la console le titre du livre parcouru.
            print(book, flush=True)

            data = book.get_data()
            response = request.request_image(data[-1])
            fileManager.get_image(response, n*20+m)
            fileManager.write(data)

    # Affiche à la console la fin de la catégorie parcouru.
    print('-'*82 + '\n', flush=True)

print('All categories have been successfully scanned.')
