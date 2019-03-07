"""
Aturan Kata imbuhan me:
- me bertemu dengan huruf vokal (aiueo) menjadi meng
- me bertemu dengan konsonan b menjadi mem
- me bertemu dengan konsonan c, d, dan j menjadi men
- me bertemu dengan konsonan g dan h menjadi meng
- me bertemu dengan konsonan l, m, n, r, w tidak mengalami perubahan

Aturan Peleburan
- me bertemu dengan konsonan k, maka k akan melebur menjadi ng
- me bertemu dengan konsonan s, maka s akan melebur menjadi ny
- me bertemu dengan konsonan t, maka t akan melebur menjadi n
- me bertemu dengan konsonan p, maka p akan melebur menjadi m
-
Syaratnya:
- diawali dengan konsonan k, t, s, p
- lebih dari satu suku kata
- suku kata awal terdiri dari konsonan dan vokal (KV) mis. kaca -> ka-ca -> k (konsonan) a (vokal)
- bila suku kata awal konsonan dan konsonan, huruf pertama tidak melebur, hanya dilakukan penambahan
mis. trak-tir -> men-trak-tir
- bila kata hanya terdiri dari satu suku kata maka imbuhannya menjadi menge. mis. bom -> mengebom
"""

import identifikasi_kata_imbuhan as iki
import perbaikan_imbuhan as pi
import re


class Stemming_Me(iki.IdentifikasiKataImbuhan, pi.PerbaikanImbuhan):

    # Pengelompokkan kata berimbuhan
    me_classification = {
        'me': [], 'me-kan': [], 'me-i': [],
        'mem': [], 'memper': [], 'memper-kan': [], 'mem-kan': [], 'mem-i': [],
        'men': [], 'men-kan': [], 'men-i': [],
        'meny': [], 'meny-kan': [], 'meny-i': [],
        'meng': [], 'meng-kan': [], 'meng-i': [],
        'menge': [], 'menge-kan': [], 'menge-i': []
    }

    # Hasil stemming dari kata berimbuhan
    me_stemm = {
        'me': [], 'me-kan': [], 'me-i': [],
        'mem': [], 'memper': [], 'memper-kan': [], 'mem-kan': [], 'mem-i': [],
        'men': [], 'men-kan': [], 'men-i': [],
        'meny': [], 'meny-kan': [], 'meny-i': [],
        'meng': [], 'meng-kan': [], 'meng-i': [],
        'menge': [], 'menge-kan': [], 'menge-i': []
    }

    # Kumpulan kata dasar dari hasil stemming
    me_katdas = {
        'me': [], 'me-kan': [], 'me-i': [],
        'mem': [], 'memper': [], 'memper-kan': [], 'mem-kan': [], 'mem-i': [],
        'men': [], 'men-kan': [], 'men-i': [],
        'meny': [], 'meny-kan': [], 'meny-i': [],
        'meng': [], 'meng-kan': [], 'meng-i': [],
        'menge': [], 'menge-kan': [], 'menge-i': []
    }

    # Klasifikasikan kata yang berimbuhan ke dalam jenis imbuhannya
    def create_me_classfication(self):
        for i in self.get_me():
            if re.match(r'memper\w+kan$', i):
                self.store_to_dict_me('memper-kan', i, 'memper', 'kan')

            elif re.match(r'memper\w+', i):
                self.store_to_dict_me('memper', i, 'memper')

            # Karena imbuhan mem berpotensi ada peleburan dan ada juga
            # kata yang diawali huruf m, maka perlu dicek ke dalam KBBI
            elif re.match(r'mem\w+kan$', i):
                res1 = ''.join(re.findall(r'mem(\w+)kan$', i))
                res2 = ''.join(re.findall(r'me(\w+)kan$', i))

                self.me_lebur_or_asli(res1, res2, 'me-kan', 'mem-kan', i, 'mem', 'kan')

            elif re.match(r'mem\w+i$', i):
                res1 = ''.join(re.findall(r'mem(\w+)i$', i))
                res2 = ''.join(re.findall(r'me(\w+)i$', i))

                self.me_lebur_or_asli(res1, res2, 'me-i', 'mem-i', i, 'mem', 'i')

            elif re.match(r'mem\w+', i):
                res1 = ''.join(re.findall(r'mem(\w+)', i))
                res2 = ''.join(re.findall(r'me(\w+)', i))

                self.me_lebur_or_asli(res1, res2, 'me', 'mem', i, 'mem')

            elif re.match(r'meny\w+kan$', i):
                res1 = ''.join(re.findall(r'meny(\w+)kan$', i))
                res2 = ''.join(re.findall(r'me(\w+)kan$', i))

                self.me_lebur_or_asli(res1, res2, 'me-kan', 'meny-kan', i, 'meny', 'kan')

            elif re.match(r'meny\w+i$', i):
                res1 = ''.join(re.findall(r'meny(\w+)i$', i))
                res2 = ''.join(re.findall(r'me(\w+)i$', i))

                self.me_lebur_or_asli(res1, res2, 'me-i', 'meny-i', i, 'meny', 'i')

            elif re.match(r'meny\w+', i):
                res1 = ''.join(re.findall(r'meny(\w+)', i))
                res2 = ''.join(re.findall(r'me(\w+)', i))

                self.me_lebur_or_asli(res1, res2, 'me', 'meny', i, 'meny')

            # elif re.match(r'menge\w+kan$', i):
            #     self.store_to_dict('menge-kan', i, 'menge', 'kan')
            #
            # elif re.match(r'menge\w+i$', i):
            #     self.store_to_dict('menge-i', i, 'menge', 'i')
            #
            # elif re.match(r'menge\w+', i):
            #     self.store_to_dict('menge', i, 'menge')

            elif re.match(r'meng\w+kan$', i):
                res1 = ''.join(re.findall(r'meng(\w+)kan$', i))
                res2 = ''.join(re.findall(r'me(\w+)kan$', i))

                self.me_lebur_or_asli(res1, res2, 'me-kan', 'meng-kan', i, 'meng', 'kan')

            elif re.match(r'meng\w+i$', i):
                res1 = ''.join(re.findall(r'meng(\w+)i$', i))
                res2 = ''.join(re.findall(r'me(\w+)i$', i))

                self.me_lebur_or_asli(res1, res2, 'me-i', 'meng-i', i, 'meng', 'i')

            elif re.match(r'meng\w+', i):
                res1 = ''.join(re.findall(r'meng(\w+)', i))
                res2 = ''.join(re.findall(r'me(\w+)', i))

                self.me_lebur_or_asli(res1, res2, 'me', 'meng', i, 'meng')

            elif re.match(r'men\w+kan$', i):
                res1 = ''.join(re.findall(r'men(\w+)kan$', i))
                res2 = ''.join(re.findall(r'me(\w+)kan$', i))

                self.me_lebur_or_asli(res1, res2, 'me-kan', 'men-kan', i, 'men', 'kan')

            elif re.match(r'men\w+i$', i):
                res1 = ''.join(re.findall(r'men(\w+)i$', i))
                res2 = ''.join(re.findall(r'me(\w+)i$', i))

                self.me_lebur_or_asli(res1, res2, 'me-i', 'men-i', i, 'men', 'i')

            elif re.match(r'men\w+', i):
                res1 = ''.join(re.findall(r'men(\w+)', i))
                res2 = ''.join(re.findall(r'me(\w+)', i))

                self.me_lebur_or_asli(res1, res2, 'me', 'men', i, 'men')

            elif re.match(r'me\w+kan$', i):
                self.store_to_dict_me('me-kan', i, 'me', 'kan')

            elif re.match(r'me\w+i$', i):
                self.store_to_dict_me('me-i', i, 'me', 'i')

            else:
                self.store_to_dict_me('me', i, 'me')

    # Mencetak frekuensi imbuhan disertai dengan kata yang muncul(unik)
    def result_me(self):
        for k, v in self.me_classification.items():
            print("imbuhan: {imb}\nfreq: {freq}".format(imb=k, freq=len(self.me_classification.get(k))))
            tmp = list(set(v))
            for word in tmp:
                print(word+", ", end="")
            print("\n")
            print('Stemm: ', end="")
            for stemm in list(set(self.me_stemm.get(k))):
                print(stemm+", ", end="")
            print("\n")
            print('Katdas: ', end="")
            for katdas in list(set(self.me_katdas.get(k))):
                print(katdas+", ", end="")
            print('\n---------------------------------------------------------')

