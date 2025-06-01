cobalist = {1,2,3,4,5}
cobalistlagii = [2,1,3,4,32]
print(cobalist)

for i in cobalistlagii:
    print(i)


random = {"1", "2", "3", "4"}
for j in random:
    print(j)


gatau = set()
gatau.add('adwswwwwwws')
gatau.add('kensa')
print(len(gatau))

gatau.add('apa ya????')
for plat in gatau:
    print(plat)

bilangan = {1, 45, 2, 34, 5, 3, 12, 31, 54}
bilangan.add(11)
print(bilangan)

kelaspro = {"aaa", "bb", "ccc"}
kelasnub = {"aaa", "bb", "zzzz"}

resultunion = kelaspro.union(kelasnub)
resultunion2 = kelaspro | kelasnub
result2 = kelaspro - kelasnub
result3 = kelasnub - kelaspro
result5 = kelaspro.union(kelasnub) - (kelaspro & kelasnub)
resultintersection = kelaspro & kelasnub
resultintersection2 = kelaspro.intersection(kelasnub)
resultsymetricdiffrence = kelaspro.symmetric_difference(kelasnub)
resultsymetricdiffrence2 = kelaspro ^ kelasnub
print(resultsymetricdiffrence2)








def unique_sum(list):
    data_set = set(list)
    total = 0
    for data in data_set:
        total = total + data
    return total

ya = [1,2,3,4,5,6,7,7,7,7]
hasil1 = unique_sum(ya)
print(hasil1)



def cek_duplikat(string):
    karakter_set = set()
    for karakter in string:
        if karakter in karakter_set:
            return True
        else:
            karakter_set.add(karakter)
    return False

string1 = 'The quick brown fox jumps over the lazy dog' 
print(cek_duplikat(string1))
string2 = 'lorem ipsum'
print(cek_duplikat(string2))






n = int(input('Masukkan jumlah kategori: '))

data_aplikasi = {}


for i in range(n):
    nama_kategori = input('Masukkan nama kategori: ')
    print('Masukkan 5 nama aplikasi di kategori', nama_kategori)
    

    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)

    data_aplikasi[nama_kategori] = aplikasi

print('\nData aplikasi per kategori:')
print(data_aplikasi)

daftar_aplikasi_list = []
for aplikasi in data_aplikasi.values():
    daftar_aplikasi_list.append(set(aplikasi))

print('\nDaftar aplikasi (dalam bentuk set per kategori):')
print(daftar_aplikasi_list)

hasil = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    hasil = hasil.intersection(daftar_aplikasi_list[i])

print('\nAplikasi yang sama di semua kategori:')
print(hasil)
