import random

class Melodii:
    def __init__(self, lista_melodii):
        self.lista_melodii = lista_melodii
        print(type(lista_melodii))
        

    def Amestec(self):
        random.shuffle(self.lista_melodii)
        return(self.lista_melodii)

playlist = Melodii (['still dre', 'god\'s gonna cut you down', 'watch your back'])
print(playlist.Amestec())







# def amestec(shit):
#      random.shuffle(shit)
#      return shit
     
     


# print(amestec(['kk','bs','dwsa','rvdc']))































