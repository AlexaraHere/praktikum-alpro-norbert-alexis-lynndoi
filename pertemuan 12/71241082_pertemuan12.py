'soal 1'

def falsetrue(a):
    sama = True
    for i in a :
        if i != a[0]:
            sama = False
    print(sama)
    return ""

print(falsetrue((1,2,3,4,5)))
print(falsetrue((32424324,213123,1)))
print(falsetrue((50,50,50)))



"soal 2"
def data_diri(wa):
    list1 = []
    for i in str(wa[0]).split():
        list1.append(i)
    list1.reverse()
    nama = wa[0]
    nim = wa[1]
    alamat = wa[2]
    print(f"NIM: {nim}")
    print(f"NAMA: {nama}")
    print(f"ALAMAT: {alamat}")
    nama_depan = tuple(nama.split()[0].lower())
    nim = tuple(nim)
    print(f"NIM: {nim}")
    print(f"NAMA DEPAN: {nama_depan}")
    print(f"NAMA TERBALIK: {list1}")
data_diri(("norbert alexis lynndoi", "71241082", "sempu, sleman"))


'soal 3'
file = input("Masukkan nama file: ")
lines = open(file)
a = dict()

for i in lines:
    if i.startswith("From "):
        misah = i.split()
        misah5 = misah[5]
        jam = misah5.split(":")[0]
        a[jam] = a.get(jam, 0) + 1

for j in sorted(a):
    print(j, a[j])