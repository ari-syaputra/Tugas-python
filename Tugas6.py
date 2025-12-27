def nilai():
    try:
        jumlah_nilai = int(input("Masukkan jumlah nilai yang akan diinput: "))
    except ValueError:
        print("Input tidak valid. Masukkan angka bulat.")
        return
    
    nilai_list = []
    for i in range(jumlah_nilai):
        try:
            nilai = float(input(f"Masukkan nilai ke-{i+1}: "))
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
            continue
        nilai_list.append(nilai)

    if not nilai_list:
        print("Tidak ada nilai yang valid untuk dihitung.")
        return
    
    rata_rata = sum(nilai_list)
    panjang = len(nilai_list)
    rata_rata /= panjang
    if rata_rata >= 75:
        status = "Lulus"
    else:
        status = "Tidak Lulus"

    print("\n=== Hasil Penilaian ===")
    print(f"Rata-rata dari {panjang} nilai yang diinput adalah: {rata_rata}")
    print(f"Status: {status}")

if __name__ == "__main__":
    nilai()