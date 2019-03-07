import stemming_ter as st
import re


class Stemming_Ke(st.Stemming_Ter):

    ke_classification = {
        'ke': [], 'ke-an': []
    }

    ke_stemm = {
        'ke': [], 'ke-an': []
    }

    ke_katdas = {
        'ke': [], 'ke-an': []
    }

    def create_ke_classification(self):
        for i in self.get_ke():
            if re.match(r'\bke\w+an\b', i):
                self.store_to_dict_ke('ke-an', i, 'ke', 'an')

            elif re.match(r'\bke\w+', i):
                self.store_to_dict_ke('ke', i, 'ke')

    def result_ke(self):
        for k, v in self.ke_classification.items():
            print("imbuhan: {imb}\nfreq: {freq}".format(imb=k, freq=len(self.ke_classification.get(k))))
            tmp = list(set(v))
            for word in tmp:
                print(word+", ", end="")
            print("\n")
            print('Stemm: ', end="")
            for stemm in list(set(self.ke_stemm.get(k))):
                print(stemm+", ", end="")
            print("\n")
            print('Katdas: ', end="")
            for katdas in list(set(self.ke_katdas.get(k))):
                print(katdas+", ", end="")
            print('\n---------------------------------------------------------')
