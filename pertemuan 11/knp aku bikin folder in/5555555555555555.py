import re
nama = input('Masukkan nama file: ')
try:
    a = open(nama)
except:
    print('File tidak bisa dibuka:', nama)
    exit()
wa = dict()
for i in a:
    i = i.lower()
    kata = re.findall(r'\b[a-z]+\b', i)
    for j in kata:
        wa[j] = wa.get(j, 0) + 1
print(wa)