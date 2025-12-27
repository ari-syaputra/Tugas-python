print("Jika user input 0, berhenti!!")
genap = 0
ganjil = 0

while True:
    try:
        angka = int(input("Masukkan angka (negatif untuk keluar): "))
    except :
        print("Input tidak valid. Masukkan angka bulat.")
        
        if angka % 2 == 0:
            genap += angka
        else:  
            ganjil += angka
            
        if angka < 0:
            break

print("Program selesai.")
print(f"Jumlah angka genap: {genap}")
print(f"Jumlah angka ganjil: {ganjil}")