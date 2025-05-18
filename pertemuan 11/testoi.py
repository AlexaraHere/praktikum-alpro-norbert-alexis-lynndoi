eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
print(eng2sp['two'])
len(eng2sp)
'one' in eng2sp
'uno' in eng2sp
vals = list(eng2sp.values())
print(vals)
'uno' in vals
vals2 = list(eng2sp.keys())
print(vals2)



word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)


word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c,0) + 1
print(d)


# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File cannot be opened:', fname)
#     exit()

# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words: 
#         if word.istitle():
#             if word in counts:
#                 counts[word] += 1
#             else:
#                 counts[word] = 1

# print(counts)


counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
print(counts)
for key in counts:
    print(key, counts[key])


import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)
