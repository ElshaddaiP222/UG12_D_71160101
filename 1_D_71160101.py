d1 = int(input("Masukkan awal deret: "))
d2 = int(input("Masukkan akhir deret: "))

for hasil in range (d1, d2):
    if hasil %2==0 and hasil % 3 != 0 and hasil % 7 != 0 :
      print(hasil, end=" ")