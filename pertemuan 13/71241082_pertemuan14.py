"soal 1"
def kategoriAplikasi():
    n = int(input('Masukkan jumlah kategori: '))
    data_aplikasi = {}

    for i in range(n):
        nama_kategori = input('Masukkan nama kategori: ')
        print('Masukkan 5 nama aplikasi di kategori', nama_kategori)

        apk = []
        for j in range(5):
            nama_aplikasi = input('Nama aplikasi: ')
            apk.append(nama_aplikasi)

        data_aplikasi[nama_kategori] = apk

    print("\nData aplikasi per kategori:")
    print(data_aplikasi)

    listapk = []
    for apk in data_aplikasi.values():
        listapk.append(set(apk))

    banyakapk = {}

    for apkset in listapk:
        for app in apkset:
            if app in banyakapk:
                banyakapk[app] += 1
            else:
                banyakapk[app] = 1

    adasatu = []
    for app in banyakapk:
        if banyakapk[app] == 1:
            adasatu.append(app)

    print("\nAplikasi yang hanya muncul di satu kategori:")
    print(adasatu)

    if n > 2:
        adadua = []
        for app in banyakapk:
            if banyakapk[app] == 2:
                adadua.append(app)
        print("\nAplikasi yang muncul tepat di dua kategori:")
        print(adadua)

kategoriAplikasi()






"soal 2"
list1 = ['ya', 'ta', 'ra', 'ea', 'wa']
print("awal nya list:", list1)
listkeset = set(list1)
print("list ke set:", listkeset)


set1 = {'a', 'b', 'c', 'd'}
print("awal nya set:", set1)
setkelist = list(set1)
print("set ke list:", setkelist)

tupple1 = ("aywau", "kakaw", "yawas", "tola")
print("awal nya Tuple:", tupple1)
tupplekeset = set(tupple1)
print("tuple ke set:", tupplekeset)

set2 = {1, 2, 3, 4}
print("awal nya Set:", set2)
setketupple = tuple(set2)
print("set ke tupple:", setketupple)



"soal 3"
def file():
    file1 = input("File 1: ")
    file2 = input("File 2: ")
    with open(file1,"r") as file:
        file1 = set(i.lower().strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"') for i in (file.read().split()))
    with open(file2,"r") as file:
        file2 = set(i.lower().strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"') for i in (file.read().split()))
    print(file1 & file2)
file()