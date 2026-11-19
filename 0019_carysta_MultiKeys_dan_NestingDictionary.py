import datetime
import string
import random

buku_template = {
    'judul buku': 'judul',
    'penulis': 'penulis',
    'tahun_terbit': 0,
    'tanggal_terakhir_pinjam': datetime.datetime(1111, 1, 1),
    'status': 'tersedia'
}

data_buku = {}

while True:
    print("\n" + "="*30)
    print("DATA PERPUSTAKAAN")
    print("="*30)

    buku = dict.fromkeys(buku_template.keys())

    buku['judul_buku'] = input("judul buku: ")
    buku['penulis'] = input("penulis: ")
    buku['tahun_terbit'] = int(input("tahun terbit: "))

    TAHUN = int(input("tahun terakhir pinjam (YYYY): "))
    BULAN = int(input("bulan terakhir pinjam (1-12): "))
    TANGGAL = int(input("tanggal terakhir pinjam (1-31): "))

    buku['tanggal_terakhir_pinjam'] = datetime.datetime(
        TAHUN, BULAN, TANGGAL
    )

    buku['status'] = input("status (tersedia/tidak): ")

    KEY = ''.join(
        random.choice(string.ascii_uppercase) for i in range(6)
    )

    #multi keys menggunakan tuple
    KEYS = (KEY, buku['tahun_terbit'])

    #memasukkan data ke dictionary
    data_buku.update({KEYS:buku})

    #menampilkan data buku
    print("\n" + "="*75)
    print("DAFTAR BUKU PERPUSTAKAAN")
    print("="*75)

    print(f"{'KEYS':<18} {'JUDUL BUKU':<20} {'PENULIS':<8} {'TAHUN TERBIT':<13} {'TGL PINJAM':<13} {'STATUS':<10}")
    print("-"*70)

    for KEY in data_buku:

        KEYS = KEY
        JUDUL = data_buku[KEY]['judul_buku']
        PENULIS = data_buku[KEY]['penulis']
        TAHUN = data_buku[KEY]['tahun_terbit']
        TANGGAL = data_buku[KEY]['tanggal_terakhir_pinjam'].strftime("%d-%m-%Y")
        STATUS = data_buku[KEY]['status']

        print(f"{str(KEYS):<18} {JUDUL:<20} {PENULIS:<18} {TAHUN:<8} {TANGGAL:<13} {STATUS:<10}")

    print("\n")
    is_done = input("mau tambah buku lagi? (y/n): ")

    if is_done == "n":
        break

print("\nAkhir dari program, terima kasih!")