def Data_Nama ():
    print("|Ketik 'exit' untuk keluar dari program.|")
    print("=========================================")
    nama = input("Masukkan nama: ")
    return nama

def Data_Prodi ():
    print("\n=========================================")
    print("|    Prodi yang tersedia: TI, SI, DK     |")
    print("=========================================")
    prodi = input("Masukkan program studi: ")
    return prodi

def Input_Nilai(mk_list):
    print("=========================================")
    nilai = []

    for mata_kuliah in mk_list:
        while True: 
            try:
                N = int(input(f"Masukkan nilai untuk mata kuliah {mata_kuliah}: "))
                break
            except ValueError:
                print("Input tidak valid. Masukkan angka!")

        nilai.append(N)

    rata_rata = sum(nilai) / len(mk_list)
    return rata_rata


def Prodi_TI():
    TI = ["Algoritma", "Basis Data", "Jaringan Komputer"]
    return Input_Nilai(TI)

def Prodi_SI():
    SI = ["Manajemen SI", "Analisis Sistem", "Sistem Enterprise"]
    return Input_Nilai(SI)

def Prodi_DK():
    DK = ["Desain Grafis", "Multimedia", "Animasi"]
    return Input_Nilai(DK)


data = []
while True:
    print("=========================================")
    nama = Data_Nama()
    if nama.lower() == "exit":
        break

    prodi = Data_Prodi()
    if prodi == "TI":
        rata_rata = Prodi_TI()
        data.append((nama, prodi, rata_rata))
    elif prodi == "SI":
        rata_rata = Prodi_SI()
        data.append((nama, prodi, rata_rata))
    elif prodi == "DK":
        rata_rata = Prodi_DK()
        data.append((nama, prodi, rata_rata))
    else:
        print("Prodi tidak valid. Harap masukkan prodi yang tersedia.")

print("\n--- Hasil Akhir ---")
if not data:
    print("Tidak ada data untuk ditampilkan.")

for entry in data:
    nama, prodi, rata_rata = entry
    print(f"Nama: {nama}, Prodi: {prodi}")
    print(f"Rata-rata Nilai: {rata_rata}")
    if rata_rata >= 65:
        status = "Lulus"
    else:
        status = "Tidak Lulus"
    print(f"Status: {status}")