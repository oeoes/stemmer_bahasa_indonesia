import stemming_se as ss
import re


class Stemming_Ter(ss.Stemming_Se):

    ter_classification = {
        'ter': [], 'ter-kan': [], 'ter-an': []
    }

    ter_stemm = {
        'ter': [], 'ter-kan': [],  'ter-an': []
    }

    ter_katdas = {
        'ter': [], 'ter-kan': [], 'ter-an': []
    }

    def create_ter_classification(self):
        for i in self.get_ter():
            if re.match(r'\bter\w+kan\b', i):
                self.store_to_dict_ter('ter-kan', i, 'ter', 'kan')

            elif re.match(r'\bter\w+an\b', i):
                self.store_to_dict_ter('ter-an', i, 'ter', 'an')

            elif re.match(r'\bter\w+', i):
                self.store_to_dict_ter('ter', i, 'ter')

    def result_ter(self):
        for k, v in self.ter_classification.items():
            print("imbuhan: {imb}\nfreq: {freq}".format(imb=k, freq=len(self.ter_classification.get(k))))
            tmp = list(set(v))
            for word in tmp:
                print(word+", ", end="")
            print("\n")
            print('Stemm: ', end="")
            for stemm in list(set(self.ter_stemm.get(k))):
                print(stemm+", ", end="")
            print("\n")
            print('Katdas: ', end="")
            for katdas in list(set(self.ter_katdas.get(k))):
                print(katdas+", ", end="")
            print('\n---------------------------------------------------------')
