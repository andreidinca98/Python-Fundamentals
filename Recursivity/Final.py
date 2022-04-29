import os.path
from os import path


#os.chdir(r'C:\Users\Cucu\Desktop\teste-python\1')


# def read_first_line(filename):+-
#     with open(filename) as f:
#         print (f.readline())
# # for filename in os.listdir(os.getcwd()):
# #     if os.path.isfile(filename): read_first_line(filename)



####   Aici am facut parcurgerea recursiva a directorului, mi se printeaza atat pathul(folderele) cat si fisierele acestora
# for path,dirnames, filenames in os.walk('1'):
#     #print('{}---{}'.format(repr(path), repr(filenames)))

    





# lista=[]
# for files in filenames:
#     files.readline()
#     lista.append(files)

















# Ce urmeaza de facut?

## Citirea primului rand din fiecare fisier, folosind readline()  -DONE

## in cheie voi avea path+filenames









#################################################################                   Teste cu os.walk care merg          #######################
###### citeste primul rand din fiecare fisier
# import os


# for dirpath,dir,files in os.walk('1'):
#     for filename in files:
#         fname=os.path.join(dirpath,filename)
#         with open(fname) as myfile:
#             g=myfile.readline()
#             print(g)

















###################################################################      Inspirat de pe ent                  ####################################
# def search(root):
#     items = os.listdir(root)
#     for item in items:
#         if os.path.isdir(item):
#             print('[-]', item)
#             search(os.path.join(root, item))
#             print (items)
# search('1' )













#######################################################################             Prototip   Recursiv         ########################

# def search(root):
#     items = os.listdir(root)
    
#     for element in items:
#         if os.path.isfile(os.path.join(root, element)):
        
#             print(element)
#         elif os.path.isdir(os.path.join(root, element)):
#             search(os.path.join(root,element))
#             print(element)

# search('1')










#####################################################################   Varianta care functioneaza!   ###########################


##### Pentru subpunctul b) se decomenteaza liniile 155 si 156 care vor face 'salt'peste fisierul 3 care are cuvantul 'stop'





import os

def search(root):

    my_dict = {}   #dictionarul in care se vor pune informatiile

    for element in os.listdir(root):
        
        if os.path.isfile(os.path.join(root, element)):
            try: 
                with open(os.path.join(root, element)) as file:
                    # if 'stop' in file.read():
                    #     continue
                    my_dict[os.path.join(root, element)] = file.readline() # populate the dictionary
            except UnicodeDecodeError: 
                # Uneori se intampla ca fisierele sa nu poata fi citite, de aceea am pus un except care sa evite aceasta eroare
                pass

        elif os.path.isdir(os.path.join(root, element)):
            my_dict.update(search(os.path.join(root,element)))  # updatarea dictionarului

    return my_dict

print(search('1'))













