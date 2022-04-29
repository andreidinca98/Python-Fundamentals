import os.path
from os import path




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













