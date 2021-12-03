def nmax (urutangka):
    nilaimax = urutangka[0]
    for i in urutangka:
        if i > nilaimax:
            nilaimax = i
    return nilaimax

def nmin(urutangka):
    nmin = urutangka[0]
    for i in urutangka:
        if i < nmin:
            nmin = i
    return nmin     

angka = [3, 30, 100, -35, 50]
print(angka)
print("nilai terbesar : ", nmax(angka))
print("nilai terkecil : ", nmin(angka))