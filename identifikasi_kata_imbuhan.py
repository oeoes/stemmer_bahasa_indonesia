import re

# Mengelompokkan seluruh kata berimbuhan pada corpus
class IdentifikasiKataImbuhan:
    me = []
    be = []
    di = []
    pe = []
    se = []
    ke = []
    ter = []

    def __init__(self, corpus):
        self.corpus = corpus

    # Mulai identifikasi kata berimbuhan menggunakan regular expression
    def prefix_identification(self):
        words = [
            i.lower() for i in re.findall(
                r'(\bme\w+\b|\bbe\w+\b|\bdi\w+\b|\bpe\w+\b|\bse\w+\b'
                r'|\bke\w+\b|\bter\w+\b)', self.corpus, flags=re.IGNORECASE)
        ]

        for i in words:
            if re.match(r'\bme\w+\b', i):
                self.me.append(i)
            elif re.match(r'\bber\w+\b', i):
                self.be.append(i)
            elif re.match(r'\bdi\w+\b', i):
                self.di.append(i)
            elif re.match(r'\bpe\w+\b', i):
                self.pe.append(i)
            elif re.match(r'\bse\w+\b', i):
                self.se.append(i)
            elif re.match(r'\bke\w+\b', i):
                self.ke.append(i)
            else:
                self.ter.append(i)

    def get_me(self):
        return self.me

    def get_be(self):
        return self.be

    def get_di(self):
        return self.di

    def get_pe(self):
        return self.pe

    def get_se(self):
        return self.se

    def get_ke(self):
        return self.ke

    def get_ter(self):
        return self.ter
