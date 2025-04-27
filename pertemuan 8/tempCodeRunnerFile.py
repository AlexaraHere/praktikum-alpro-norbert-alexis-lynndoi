
def ke_hari(tanggal):
    if len(tanggal) != 10 or tanggal[4] != '-' or tanggal[7] != '-':
        return "Format tanggal tidak valid. Harap masukkan dalam format YYYY-MM-DD."

    y = int(tanggal[0:4])
    m = int(tanggal[5:7])
    d = int(tanggal[8:10])
    y *= 360
    m *= 30
    d *= 1
    hari_ini = ke_hari(2025, 4, 23)

    hari_input = ke_hari(y, m, d)

    return f"Selisih: {abs(hari_ini - hari_input)} hari"

a = input(ke_hari("input tanggal = "))
print(a)


