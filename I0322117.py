from anggota import tambah_anggota, cari_anggota_by_id, tampilkan_anggota, edit_anggota
from tabungansampah import tambah_tabungan, tarik_tabungan, tampilkan_tabungan
from os import system, listdir, getcwd

# Fungsi lainnya untuk membantu
def input_of_options(prompt, ls_opt):
    while True:
        try:
            masuk = input(prompt)
            assert masuk.strip() in ls_opt, "Input tidak valid!"
            break
        except AssertionError as er:
            print(er)

    return masuk.strip()

def input_normal(prompt):
    while True:
        try:
            masuk = input(prompt)
            assert len(masuk.strip()) > 0, "Input tidak boleh kosong atau hanya spasi!"
            break
        except AssertionError as er:
            print(er)

    return masuk.strip()

# Blok utama
while True:
    system("cls")
    print("""
=========================================
** Program Pengelolaan Tabungan Sampah **
=========================================
Pilihan menu :
1. Pengelolaan Keanggotaan
    1a. Penambahan Data Anggota
    1b. Pencarian Data Anggota
    1c. Pengubahan Data Anggota
2. Pengelolaan Tabungan Anggota
    2a. Penambahan Tabungan
    2b. Penarikan Tabungan
    2c. Menampilkan Data Tabungan
9. Exit
""")
    pilih = input_of_options("Masukkan menu pilihan Anda: ", ["1a", "1b", "1c", "2a", "2b", "2c", "9"])

    if pilih == "1a":
        nama = input_normal("Masukkan nama anda: ")
        alamat = input_normal("Masukkan alamat anda: ")
        telepon = input_normal("Masukkan telepon anda: ")

        tambah_anggota(nama, alamat, telepon)
    elif pilih == "1b":
        print("Pencarian data anggota")
        id_anggota = input_normal("Masukkan ID Anggota: ")

        hasil = cari_anggota_by_id(id_anggota)

        tampilkan_anggota(hasil)
    elif pilih == "1c":
        edit_anggota()
    elif pilih == "2a": 
        id_dicari = input_normal("Masukkan ID Anggota : ")
        data = cari_anggota_by_id(id_dicari)
        
        if data == {}:
            print("ID tidak ditemukan !")
            input("Tekan enter untuk melanjutkan ")
            continue
        
        print(f"""============================================= 
IDAnggota : {id_dicari:<15} | Nama  : {data["nama"]} 
Telepon   : {data["telepon"]:<15} | Alamat: {data["alamat"]} 
============================================= 
--------------------------------------------- 
Kode    | Jenis Sampah  | Harga Satuan (Rp)     
--------------------------------------------- 
1       | Kardus        |  500      
2       | Botol plastic |  300 
3       | Logam besi    |  800 
4       | Tembaga       | 1000 
---------------------------------------------""")
        
        kode = input_of_options("Pilih jenis sampah     : ", ["1", "2", "3", "4"])
            
        while True:
            try:
                kuantitas = float(input("Kuantitas sampah       : "))
                break
            except ValueError:
                print("Input tidak valid !")
        
        tambah_tabungan(id_dicari, kode, kuantitas)
        
    elif pilih == "2b":
        id_dicari = input_normal("Masukkan ID Anggota : ")
        data = cari_anggota_by_id(id_dicari)
        
        if data == {}:
            print("ID tidak ditemukan !")
            input("Tekan enter untuk melanjutkan ")
            continue
        
        if f"tabungan{id_dicari}.json" not in listdir(getcwd()):
            print("Belum memiliki tabungan!")
            input("Tekan enter untuk melanjutkan ")
            continue
        
        tarik_tabungan(id_dicari)
        
    elif pilih == "2c":
        id_dicari = input_normal("Masukkan ID Anggota : ")
        data = cari_anggota_by_id(id_dicari)
        
        if data == {}:
            print("ID tidak ditemukan !")
            input("Tekan enter untuk melanjutkan ")
            continue
        
        if f"tabungan{id_dicari}.json" not in listdir(getcwd()):
            print("Belum memiliki tabungan!")
            input("Tekan enter untuk melanjutkan ")
            continue
        
        tampilkan_tabungan(id_dicari)
        
    elif pilih == "9":
        print("Anda Keluar dari program. Terima Kasih !")
        break
