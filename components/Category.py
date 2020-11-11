'''
Cette classe permet d'initialiser toutes les URLS
d'une catégorie en fonction du nombre de page.
Une méthode lui permet d'associer toutes les URLS
des livres situé dans une page.
'''


class Category:

    def __init__(self, url='', html=''):
        self.url = url

        # Récupère le nom de la catégorie situé à
        # partir du 52ème caractère de l'URL
        self.name = url[51:].split('_')[0]
        self.pages = {}

        # On regarde si il existe plus d'une page et
        # on affecte le nombre de page à un attribut
        # page. On stock dans une liste les URLS.
        try:
            self.page = int(html.find(
                'li',
                {'class': 'current'}
                ).text.split()[-1])
            self._get_pages()

        except Exception:
            self.page = 1
            self.pages[url] = ''

    def _get_pages(self):
        for page in range(self.page):

            # On crée les URLS des catégories qui ont
            # plusieurs pages en remplacant le dernier
            # tronçons de l'URL par '/page-{n}.html'.
            self.pages[('/'.join(self.url.split('/')[:-1]) +
                        '/page-{}.html'.format(page+1))] = ''

    def get_books(self, url, html):
        # Test si les critères de recherche sont toujours bon.
        try:
            books = html.findAll(
                'li',
                {'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'}
                )

            # On rempli le dictionnaire ou les clés sont les
            # URL des pages et les valeurs la liste des URLS
            # des livres contenu.
            self.pages[url] = [
                ('http://books.toscrape.com/catalogue' +
                 book.find('a')['href'][8:])
                for n, book in enumerate(books)]
        except Exception:
            print("The criteria are not suitable," +
                  "check them on the url: {}".format(url))

    # Méthode pour afficher les instances de manière
    # plus approprié.
    def __str__(self):
        title = ("\n{} category: {} --> {} page(s) {}\n"
                 .format('-'*25,self.name, self.page, '-'*25))
        url = "\n{}url: {}".format(' '*3, self.url)
        return title + url
