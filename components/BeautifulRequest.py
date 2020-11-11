'''
Cette classe automatise les requêtes et permet de récupérer le
code HTML.
Elle récupère également toutes les URLS des catégories.
Permet de faire une requête pour obtenir le contenu d'une
image.
'''

import requests
from bs4 import BeautifulSoup


class BeautifulRequest:
    def __init__(self, url):
        self.url = url

    def get_urls(self):

        # Test si les critères de selection sont correct
        try:

            # On récupère le HTML de la page d'accueil
            # et on retoune une liste d'URLS des catégories.
            html = self.get_html(self.url)
            urls = (html.find('ul', {'class': 'nav nav-list'})
                    .find('ul').findAll('a'))
            urls = [self.url + url['href'] for url in urls]
        except Exception:
            print("The criteria are not suitable, check them on the url: {}"
                  .format(self.url))
        return urls

    def get_html(self, url):

        # On test si la requête est fonctionnelle et
        # on retourne le code HTML de la page.
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        return BeautifulSoup(response.text, 'html.parser')

    def request_image(self, url):
        try:
            response = requests.get(url).content
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        return response



# Permet de tester la classe.
if __name__ == '__main__':
    url = 'http://books.toscrape.com/'
    soup = BeautifulRequest()
    html = soup.get_html(url)
    print(html)
