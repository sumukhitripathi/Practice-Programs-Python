#Binary file operations

import pickle

with open('input.dat', 'wb') as file_obj:
    data = ["This is a binary file"]
    pickle.dump(data, file_obj)
    print("Data entered into file")

with open('input.dat', 'rb') as file_load:
    text = pickle.load(file_load)
    print("Data in file: ")
    print(text)