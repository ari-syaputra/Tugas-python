total = 0 

while True:
    nama = input("Masukkan nama (ketik 'selesai' untuk keluar): ")
    if nama.lower() == 'selesai':
        break
    try:
        harga = float(input("Masukkan harga barang: "))
    except ValueError:
        print("harus masukan angka")

    total += harga


if total >= 500000:
    diskon = "Diskon 30%"
    diskon_nilai = (30 / 100) * total
    diskon_terapan = total - diskon_nilai
elif total >= 200000:
    diskon = "Diskon 20%"
    diskon_nilai = (20 / 100) * total
    diskon_terapan = total - diskon_nilai
elif total >= 100000:
    diskon = "Diskon 10%"
    diskon_nilai = (10 / 100) * total
    diskon_terapan = total - diskon_nilai
else:
    diskon = "Tidak ada diskon"
    diskon_nilai = 0
    diskon_terapan = total

print("\n=== Rincian Pembelian ===")
print(f"Total Belanja: Rp{total:,.2f}")
print(f"{diskon}: Rp{diskon_nilai:,.2f}")
print(f"Total Setelah Diskon: Rp{diskon_terapan:,.2f}")
print("==============================================================")