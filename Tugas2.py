def input_jumlah_mahasiswa():
    while True:
        try:
            jumlah = int(input("Masukkan jumlah mahasiswa: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0.")
                continue
            return jumlah
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

def input_nilai(pesan):
    while True:
        try:
            nilai = float(input(pesan))
            if 0 <= nilai <= 100:
                return nilai
            else:
                print("Nilai harus antara 0 dan 100.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

def hitung_nilai_akhir(tugas, uts, uas):
    return (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)

def tentukan_grade(nilai_akhir):
    if nilai_akhir >= 85:
        return 'A'
    elif nilai_akhir >= 70:
        return 'B'
    elif nilai_akhir >= 55:
        return 'C'
    elif nilai_akhir >= 40:
        return 'D'
    else:
        return 'E'
    
def proses_data_mahasiswa():
    jumlah = input_jumlah_mahasiswa()
    data_mahasiswa = []

    for i in range(jumlah):
        print(f"\nMasukkan data untuk mahasiswa ke-{i+1}:")
        nama = input("Nama: ")
        tugas = input_nilai("Nilai Tugas: ")
        uts = input_nilai("Nilai UTS: ")
        uas = input_nilai("Nilai UAS: ")

        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        grade = tentukan_grade(nilai_akhir)

        data_mahasiswa.append({
            'nama': nama,
            'tugas': tugas,
            'uts': uts,
            'uas': uas,
            'akhir': nilai_akhir,
            'grade': grade
        })

    return data_mahasiswa

def tampilkan_data_mahasiswa(data):
    print("\n==============================================================")
    print("No | Nama        | Tugas | UTS | UAS | Akhir | Grade")
    print("--------------------------------------------------------------")

    for i, mhs in enumerate(data, start=1):
        print(f"{i:<2} | {mhs['nama']:<10} | {mhs['tugas']:<5} | {mhs['uts']:<3} | {mhs['uas']:<3} | {mhs['akhir']:<5.1f} | {mhs['grade']}")

    print("==============================================================")


# PROGARAM UTAMA
data_mahasiswa = proses_data_mahasiswa()
tampilkan_data_mahasiswa(data_mahasiswa)