import stemming_ke as sk


# Aplikasi utama
class Main(sk.Stemming_Ke):

    def run_stemming(self):
        self.prefix_identification()
        self.create_be_classification()
        self.create_me_classfication()
        self.create_di_classification()
        self.create_pe_classification()
        self.create_se_classification()
        self.create_ter_classification()
        self.create_ke_classification()


# membuka file corpus
file = open('corpus.txt', 'r')

# convert binary (dari file corpus) ke dalam string / text
file = file.read()

# instantiasi
obj = Main(file)
obj.run_stemming()

obj.result_me()
print("***************************************************************\n")
obj.result_be()
print("***************************************************************\n")
obj.result_di()
print("***************************************************************\n")
obj.result_pe()
print("***************************************************************\n")
obj.result_se()
print("***************************************************************\n")
obj.result_ke()
print("***************************************************************\n")
obj.result_ter()
print("***************************************************************\n")


