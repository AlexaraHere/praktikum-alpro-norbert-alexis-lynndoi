# for i in range(10):
#     if i == 5:
#         continue
#     print(i, end=" "

def hitung_jarak_tempuh (StartVel,T0,Weather,Street,gas,traffic,weight,wheel):
    sum = 0

    for i in range (1,6):
        StartVel = Weather,gas,wheel
        T0= Street,traffic,weight
        if i % 2:
            StartVel = 0.95
            T0= 0.95
            jarak = StartVel,T0
            sum += jarak
        elif i == 2:
            StartVel= 1.1
            T0 =  1.1
            jarak = StartVel,T0
            sum += jarak
        else:
            StartVel = 1.15
            T0=  1.15
            jarak = StartVel*T0
            sum += jarak
        print(f"Jarak tempuh bulan {i}: {jarak:.2f} km")
    print(f"Total jarak tempuh selama 5 bulan: {sum:.2f} km")
hitung_jarak_tempuh(10,10,10,10,10,10,10,10)