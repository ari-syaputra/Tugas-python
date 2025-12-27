data = []

while True:
    print("="*30)
    nama = input("Masukkan nama (atau ketik 'selesai' untuk berhenti): ")
    print("="*30)
    if nama.lower() == 'selesai':
        break

    print("Prodi yang tersedia: TI, SI, DK")
    prodi = input("Masukkan prodi: ")
    print("="*30)
    if prodi == "TI":
        TI = ["Algoritma", "Basis Data", "Jaringan Komputer"]
        nilai = []
        for mata_kuliah in TI:
            try:
                N = int(input(f"Masukkan nilai untuk mata kuliah {mata_kuliah}\t: "))
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
            nilai.append(N)
        
        Panjang = len(TI)
        rata_rata = sum(nilai)
        rata_rata /= Panjang
        data.append((nama, prodi, rata_rata))
    elif prodi == "SI":
        SI = ["Manajemen Sistem Informasi", "Analisis dan Perancangan Sistem", "Sistem Informasi Enterprise"]
        nilai = []
        for mata_kuliah in SI:
            try:
                N = int(input(f"Masukkan nilai untuk mata kuliah {mata_kuliah}\t: "))
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
            nilai.append(N)
        
        Panjang = len(SI)
        rata_rata = sum(nilai)
        rata_rata /= Panjang
        data.append((nama, prodi, rata_rata))
    elif prodi == "DK":
        DK = ["Desain Grafis", "Multimedia", "Animasi"]
        nilai = []
        for mata_kuliah in DK:
            try:
                N = int(input(f"Masukkan nilai untuk mata kuliah {mata_kuliah}\t: "))
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
            nilai.append(N)
        
        Panjang = len(DK)
        rata_rata = sum(nilai)
        rata_rata /= Panjang
        data.append((nama, prodi, rata_rata))
    else:
        print("Prodi tidak valid. Harap masukkan prodi yang tersedia.")

print("\n--- Hasil Akhir ---")

if not data:
    print("Tidak ada data untuk ditampilkan.")

for entry in data:
    nama, prodi, rata_rata = entry
    print(f"Nama\t\t: {nama}")
    print(f'Prodi\t\t: {prodi}')
    print(f"Rata-rata Nilai\t: {rata_rata}")
    
    if rata_rata >= 80:
        status = "Lulus"
    else:
        status = "Tidak Lulus"
    print(f"Status\t\t: {status}\n")