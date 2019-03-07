import stemming_me as sm


# Aplikasi utama
class Main(sm.Stemming_Me):

    def run_stemming(self):
        self.prefix_identification()
        self.create_me_classfication()


# membuka file corpus
file = open('corpus.txt', 'r')

# convert binary (dari file corpus) ke dalam string / text
file = file.read()

# instantiasi
obj = Main(file)
obj.run_stemming()

print(obj.result_me())
