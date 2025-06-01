def read():
    file_1 = input("Masukkan nama File 1: ")
    file_2 = input("Masukkan nama File 2: ")
    with open(file_1,"r") as file:
        file_1 = set(i.lower().strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"') for i in (file.read().split()))
    with open(file_2,"r") as file:
        file_2 = set(i.lower().strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"') for i in (file.read().split()))
    print(file_1 & file_2)
read()