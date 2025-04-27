berat = []
for i in range(10):
    test = float(input(f"berat nya bos ke {i+1} "))
    berat.append(test)

upah = 2000
target = [27,28,29,30,31,32,33] 
jumlah = 0
while jumlah < 10:
    lolos = 0
    for a in berat:
        if a in target:
            lolos += 1
    jumlah +=1



    
mbayar = lolos * upah
tidak_lolos = 10 - lolos
print(mbayar)
print(tidak_lolos)
print(lolos)
