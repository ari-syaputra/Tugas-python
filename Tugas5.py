try:
    jumlah_nilai = int(input("Masukkan jumlah nilai yang akan diinput: "))
except ValueError:
    print("Input tidak valid. Masukkan angka bulat.")
    
nilai_list = []
for i in range(jumlah_nilai):
    while True:
        try:
            nilai = float(input(f"Masukkan nilai ke-{i+1}: "))
            break
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
            continue
    nilai_list.append(nilai)

rata_rata = sum(nilai_list)
panjang = len(nilai_list)
rata_rata /= panjang
if rata_rata >= 75:
    status = "Lulus"
else:
    status = "Tidak Lulus"

print("\n=== Hasil Penilaian ===")
print(f"Rata-rata dari {jumlah_nilai} nilai yang diinput adalah: {rata_rata}")
print(f"Status: {status}")