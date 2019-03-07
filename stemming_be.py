import stemming_me as sm
import re


class Stemming_Be(sm.Stemming_Me):


    be_classification = {
        'be': [], 'be-kan': [], 'ber': [], 'ber-kan': [], 'ber-nya': []
    }

    be_stemm = {
        'be': [], 'be-kan': [], 'ber': [], 'ber-kan': [], 'ber-nya': []
    }

    be_katdas = {
        'be': [], 'be-kan': [], 'ber': [], 'ber-kan': [], 'ber-nya': []
    }

    def create_be_classification(self):
        for i in self.get_be():
            if re.match(r'ber\w+nya$', i):
                self.store_to_dict_be('ber-nya', i, 'ber', 'nya')
            elif re.match(r'ber\w+kan$', i):
                self.store_to_dict_be('ber-kan', i, 'ber', 'kan')
            elif re.match(r'ber\w+', i):
                self.store_to_dict_be('ber', i, 'ber')
            elif re.match(r'be-kan', i):
                self.store_to_dict_be('ber', i, 'ber')
            elif re.match(r'be', i):
                self.store_to_dict_be('be', i, 'be')

    def result_be(self):
        for k, v in self.be_classification.items():
            print("imbuhan: {imb}\nfreq : {freq}".format(imb=k, freq=len(self.be_classification.get(k))))

            tmp = list(set(v))
            for word in tmp:
                print(word + ", ", end="")
            print("\n")

            print('Stemm: ', end="")
            for stemm in list(set(self.be_stemm.get(k))):
                print(stemm+", ", end="")
            print("\n")
            print('Katdas: ', end="")
            for katdas in list(set(self.be_katdas.get(k))):
                print(katdas+", ", end="")
            print('\n---------------------------------------------------------')
