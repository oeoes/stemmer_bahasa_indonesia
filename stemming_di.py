import stemming_be as sb
import re


class Stemming_Di(sb.Stemming_Be):
    di_classification = {
        'di': [], 'di-kan': [], 'di-i': [], 'di-nya': []
    }

    di_stemm = {
        'di': [], 'di-kan': [], 'di-i': [], 'di-nya': []
    }

    di_katdas = {
        'di': [], 'di-kan': [], 'di-i': [], 'di-nya': []
    }

    def create_di_classification(self):
        for i in self.get_di():
            if re.match(r'di\w+nya$', i):
                self.store_to_dict_di('di-nya', i, 'di', 'nya')

            elif re.match(r'di\w+kan$', i):
                self.store_to_dict_di('di-kan', i, 'di', 'kan')

            elif re.match(r'di\w+i$', i):
                self.validate_akhiran_i(*re.findall(r'di(\w+)i$', i), 'di-i', i)

            elif re.match(r'di\w+', i):
                self.store_to_dict_di('di', i, 'di')

    def result_di(self):
        for k, v in self.di_classification.items():
            print("imbuhan: {imb}\nfreq: {freq}".format(imb=k, freq=len(self.di_classification.get(k))))
            tmp = list(set(v))
            for word in tmp:
                print(word+", ", end="")
            print("\n")
            print('Stemm: ', end="")
            for stemm in list(set(self.di_stemm.get(k))):
                print(stemm+", ", end="")
            print("\n")
            print('Katdas: ', end="")
            for katdas in list(set(self.di_katdas.get(k))):
                print(katdas+", ", end="")
            print('\n---------------------------------------------------------')
