'''
Cette classe gère la création de dossiers CSV et images,
crée des fichiers CSV, écrit des données dans les
fichiers CSV et crée des fichiers images.
'''
import os
import csv


class FileManager:
    # Les en-têtes des fichiers CSV.
    CSV_HEADERS = [
        'product_page_url',
        'universal_product_code',
        'title', 'price_including_tax',
        'price_excluding_tax',
        'number_available',
        'product_description',
        'category',
        'review_rating',
        'image_url'
        ]

    def __init__(self, category):
        self.category = category
        self.name = 'csv/books_' + category + '.csv'
        self.file = None
        self.writer = None
        self._initialize()

    def _initialize(self):
        if not os.path.exists('csv'):
            os.mkdir('csv')

        if not os.path.exists('images'):
            os.mkdir('images')

        if not os.path.exists('images/' + self.category):
            os.mkdir('images/' + self.category)

        # on regarde si il n'y a pas d'erreur avec le fichier.
        try:
            with open(self.name, 'w', newline='', encoding='utf-8') as file:
                self.file = file

                # Création d'un object ou l'on peut écrire/convertir des
                # données en csv.
                self.writer = csv.writer(self.file)

                # On ajoute les en-têtes en première ligne du fichier CSV.
                self.writer.writerow(FileManager.CSV_HEADERS)
        except IOError:
            print("Problem with the file: ", self.name)

    def write(self, data):
        # on regarde si il n'y a pas d'erreur avec le fichier
        # ouvert en mode 'ajout'.
        try:
            with open(self.name, 'a', newline='', encoding='utf-8') as file:
                self.file = file
                self.writer = csv.writer(self.file)

                # On encode et decode les données 'str' pour être sûr de
                # bien écrire les informations
                data = [d.encode('raw_unicode_escape')
                        .decode('utf-8') for d in data]
                self.writer.writerow(data)
        except IOError:
            print("Problem with the file: ", self.name)

    def get_image(self, response, n):
        try:
            with open('images/' + self.category + '/book' +
                      str(n+1)+'.jpg',  'wb') as file:
                file.write(response)
        except IOError:
            print("Problem with the file: ", self.name)


# Permet de tester la class
if __name__ == '__main__':

    file = FileManager('fiction')
    a = ['a', '2', 'c', 'd']
    file.write(a)
