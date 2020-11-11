'''
Cette classe récupère grâce a du code HTML des informations sur les
livres et les stock dans des attributs.
Elle permet de les envoyer sous forme de liste.
'''


class Book:

    # Permet de traduire la colonne 'review_rating'
    # avec un chiffre au lieu du chiffre en toutes lettres.
    NUMERATION_REVIEW_RATING = {
        'One': '1',
        'Two': '2',
        'Three': '3',
        'Four': '4',
        'Five': '5'
        }

    def __init__(self, url='', html=''):
        self.url = url

        # Test si les critères de sélection sont correct.
        try:
            self.upc = html.findAll('td')[0].text
            self.title = html.find('h1').text
            self.price_in_tax = html.findAll('td')[2].text
            self.price_ex_tax = html.findAll('td')[3].text
            self.number_available = html.findAll('td')[-2].text[10:].split()[0]
            self.description = html.findAll('p')[3].text
            self.category = (html.find('ul', {'class': 'breadcrumb'})
                             .findAll('li')[2].find('a').text)

            self.review_rating = Book.NUMERATION_REVIEW_RATING[
                                    html.find(
                                        'p',
                                        {'class': 'star-rating'},
                                        )['class'][1]]
            self.image_url = ('http://books.toscrape.com/' +
                              html.find('img')['src'][6:])
        except Exception:
            print("The criteria are not suitable, check them on the url: {}"
                  .format(self.url))

    def get_data(self):

        # On utilise le spécial attribut '__dict__' pour parcourir
        # la liste des attributs qui sont les informations du livres
        # et on les retournes dans une liste.
        return [self.__dict__[data] for data in self.__dict__]

    # Méthode pour afficher les instances de manière
    # plus approprié.
    def __str__(self):
        return '{}book: {}'.format(
            ' '*8,
            self.title,
            )
