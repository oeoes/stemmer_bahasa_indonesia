import stemming_pe as sp
import re


class Stemming_Se(sp.Stemming_Pe):

    se_classification = {
        'se': [], 'se-kan': [], 'se-i': [], 'se-nya': []
    }

    se_stemm = {
        'se': [], 'se-kan': [], 'se-i': [], 'se-nya': []
    }

    se_katdas = {
        'se': [], 'se-kan': [], 'se-i': [], 'se-nya': []
    }

    def create_se_classification(self):
        for i in self.get_se():
            if re.match(r'se\w+kan', i):
                self.store_to_dict_se('se-kan', i, 'se', 'kan')

            elif re.match(r'se\w+nya', i):
                self.store_to_dict_se('se-nya', i, 'se', 'nya')

            elif re.match(r'\bse\w+i\b', i):
                self.store_to_dict_se('se-i', i, 'se', 'i')

            elif re.match(r'se\w+', i):
                self.store_to_dict_se('se', i, 'se')

    def result_se(self):
        for k, v in self.se_classification.items():
            print("imbuhan: {imb}\nfreq: {freq}".format(imb=k, freq=len(self.se_classification.get(k))))
            tmp = list(set(v))
            for word in tmp:
                print(word + ", ", end="")
            print("\n")
            print('Stemm: ', end="")
            for stemm in list(set(self.se_stemm.get(k))):
                print(stemm + ", ", end="")
            print("\n")
            print('Katdas: ', end="")
            for katdas in list(set(self.se_katdas.get(k))):
                print(katdas + ", ", end="")
            print('\n---------------------------------------------------------')
