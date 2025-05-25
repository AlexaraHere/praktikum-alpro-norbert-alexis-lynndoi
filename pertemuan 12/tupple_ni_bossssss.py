ccccc = ('wawa', 'nene', 'polpol')
ccccc = ('A',) + ccccc[1:]
print(ccccc) 








t = tuple('waaaaaaaaaadrefe')
print(t)


m = ['do', 'wa', 'pok']
x, y, z = m
print(x)
print(y,z)

tuple1 = tuple()


waa = ('w',)
waaa = ('w')



wa = 'w', 'a', 's', 'd'


a = ('a','s','d','apalah','e')

aa = list(a)
print(aa)

b = a + ("w",)
print(b)

c = a[:-3] + ("w",)
print(c)

d = a[0:3] + a[4:5]
print(d)

e = "waaaaa"
f = a + (e,)
print(f)

g = ("ca", "da",)
h = a + g
print(h)

i = (("aaaaa", "ccccc",),("wwwwwww", "ddddd",))
j = a + i
print(j)


banding1=(0,1,200000000000)

banding2=(0,3,4)
banding3 = banding1 < banding2
print(banding3)


sort = (1,2,32,5,6,7,10,)
sort = sorted(sort)
print(sort)

asdos = {"daa": 23, "wada": 54, "wawd" : 2133,}
print(asdos.keys())
print(list(asdos.keys()))
print(list(asdos.values()))
print(list(asdos.items()))





wasa = {'ada': 101, 'bada': 12, 'cada': 42}

for key, val in wasa.items():
    print(val, key)



directory = dict()
nama_terakhir = 'lynndoi'
nama_pertama = 'nobe'
no_telp = '082133261893'
directory[(nama_terakhir, nama_pertama)] = no_telp
for nama_terakhir, nama_pertama in directory:
    print(nama_pertama, nama_terakhir, directory[(nama_terakhir, nama_pertama)])

