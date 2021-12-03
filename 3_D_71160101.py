berlian = int(input("Masukan angka : "))

for i in range(berlian):
    print(" "*(berlian-i)+" *"* (i+1))

for j in range(berlian-1):
    print(" "* (j+2)+" *"* (berlian-1-j))