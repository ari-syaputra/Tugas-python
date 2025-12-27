FILENAME = "kontak.txt"

def membaca_kontak():
    kontak = []
    try:
        f = open(FILENAME, "r")
        lines = f.read().split("\n")
        for line in lines:
            if not line:
                continue
            data = line.split(",")
            kontak.append(data)
        f.close()
    except FileNotFoundError:
        print("File tidak ditemukan. Membuat file baru.")
    return kontak

def simpan_kontak(kontak):
    """Simpan kontak ke dalam file."""
    with open(FILENAME, "w") as f:
        for c in kontak:
            f.write(c[0] + "," + c[1] + "," + c[2])

def menambah_kontak():
    nama = input("Masukkan nama: ")
    nomor = input("Masukkan nomor telepon: ")
    email = input("Masukkan email: ")

    if "@" not in email:
        print("Email tidak valid. Harus mengandung '@'.")
        return
    
    kontak = membaca_kontak()
    kontak.append((nama, nomor, email))
    simpan_kontak(kontak)
    print("Kontak berhasil ditambahkan.")

def list_contacts():
    kontak = membaca_kontak()
    if len(kontak) == 0:
        print("Tidak ada kontak.")
        return
    for i, c in enumerate(kontak):
        print(f"{i+1}. {c[0]} - {c[1]} - {c[2]}")

def mencari_kontak():
    q = input("Masukkan nama yang dicari (tekan enter untuk menampilkan semua): ")
    kontak = membaca_kontak()
    ditemukan = []

    for c in kontak:
        if q.lower() in c[0]:
            ditemukan.append(c)
    if not ditemukan:
        print("Kontak tidak ditemukan.")
    else:
        for c in ditemukan:
             print(f"{c[0]} - {c[1]} - {c[2]}")

def hapus_kontak():
    nama = input("Masukkan nama kontak yang akan dihapus: ")
    kontak = membaca_kontak()
    ditemukan = False
    for i, c in enumerate(kontak):
        if c[0].lower() == nama.lower():
            ditemukan = True
            del kontak[i]
            break
    if ditemukan:
        simpan_kontak(kontak)
        print("Kontak berhasil dihapus.")
    else:
        print("Kontak tidak ditemukan.")

def menu():
    while True:
        print("=== Menu Kontak ===")
        print("1. Tambah Kontak")
        print("2. Daftar Kontak")
        print("3. Hapus Kontak")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")
        if pilihan == "1":
            menambah_kontak()
        elif pilihan == "2":
            list_contacts()
        elif pilihan == "3":
            hapus_kontak()
        elif pilihan == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu()