import stemming_di as di
import re


class Stemming_Pe(di.Stemming_Di):

    pe_classification = {
        'pe': [], 'pe-nya': [], 'pe-kan': [], 'pe-an': [], 'pe-i': [],
        'per': [], 'per-kan': [], 'per-an': [], 'per-annya': [],
        'peng': [], 'peng-kan': [], 'peng-an': [],
        'pem': [], 'pem-an': [],
        'pen': [], 'pen-an': [], 'peny': []
    }

    pe_stemm = {
        'pe': [], 'pe-nya': [], 'pe-kan': [], 'pe-an': [], 'pe-i': [],
        'per': [], 'per-kan': [], 'per-an': [], 'per-annya': [],
        'peng': [], 'peng-kan': [], 'peng-an': [],
        'pem': [], 'pem-an': [],
        'pen': [], 'pen-an': [], 'peny': []
    }

    pe_katdas = {
        'pe': [], 'pe-nya': [], 'pe-kan': [], 'pe-an': [], 'pe-i': [],
        'per': [], 'per-kan': [], 'per-an': [], 'per-annya': [],
        'peng': [], 'peng-kan': [], 'peng-an': [],
        'pem': [], 'pem-an': [],
        'pen': [], 'pen-an': [], 'peny': []
    }

    def create_pe_classification(self):
        for i in self.get_pe():
            if re.match(r'\bpem\w+an\b', i):
                self.store_to_dict_pe('pem-an', i, 'pem', 'an')

            elif re.match(r'\bpem\w+', i):
                res1 = ''.join(re.findall(r'pem(\w+)', i))
                res2 = ''.join(re.findall(r'pe(\w+)', i))

                self.pe_lebur_or_asli(res1, res2, 'pe', 'pem', i, 'pem')

            elif re.match(r'\bper\w+kan\b', i):
                self.store_to_dict_pe('per-kan', i, 'per', 'kan')

            elif re.match(r'\bper\w+annya\b', i):
                self.store_to_dict_pe('per-annya', i, 'per', 'annya')

            elif re.match(r'\bper\w+an\b', i):
                self.store_to_dict_pe('per-an', i, 'per', 'an')

            elif re.match(r'\bper\w+', i):
                self.store_to_dict_pe('per', i, 'per')

            elif re.match(r'\bpeng\w+kan\b', i):
                self.store_to_dict_pe('peng-kan', i, 'peng', 'kan')

            elif re.match(r'\bpeng\w+an\b', i):
                self.store_to_dict_pe('peng-an', i, 'peng', 'an')

            elif re.match(r'\bpeng\w+', i):
                self.store_to_dict_pe('peng', i, 'peng')

            elif re.match(r'\bpeny\w+', i):
                self.store_to_dict_pe('peny', i, 'peny')

            elif re.match(r'\bpen\w+an\b', i):
                self.store_to_dict_pe('pen', i, 'pen', 'an')

            elif re.match(r'\bpen\w+', i):
                self.store_to_dict_pe('pen', i, 'pen')

            elif re.match(r'\bpe\w+nya\b', i):
                self.store_to_dict_pe('pe-nya', i, 'pe', 'nya')

            elif re.match(r'\bpe\w+kan\b', i):
                self.store_to_dict_pe('pe-kan', i, 'pe', 'kan')

            elif re.match(r'\bpe\w+an\b', i):
                self.store_to_dict_pe('pe-an', i, 'pe', 'an')

            elif re.match(r'\bpe\w+i\b', i):
                self.store_to_dict_pe('pe-i', i, 'pe', 'i')

            elif re.match(r'\bpe\w+', i):
                self.store_to_dict_pe('pe', i, 'pe')

    def result_pe(self):
        for k, v in self.pe_classification.items():
            print("imbuhan: {imb}\nfreq: {freq}".format(imb=k, freq=len(self.pe_classification.get(k))))
            tmp = list(set(v))
            for word in tmp:
                print(word+", ", end="")
            print("\n")
            print('Stemm: ', end="")
            for stemm in list(set(self.pe_stemm.get(k))):
                print(stemm+", ", end="")
            print("\n")
            print('Katdas: ', end="")
            for katdas in list(set(self.pe_katdas.get(k))):
                print(katdas+", ", end="")
            print('\n---------------------------------------------------------')
