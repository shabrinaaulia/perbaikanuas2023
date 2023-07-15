# 2) A 
from json import load,dump
from datetime import date
from random import choices
from os import path, getcwd, system

# Fungsi Membuat ID Anggota
def generate_idanggota():
    ls_hruf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ls_ang = "0123456789"
    return ''.join(choices(ls_ang, k=5))

# Fungsi Menambah Anggota
def tambah_anggota(nama, alamat, telp):
    # Buka JSON 
    with open(path.join(getcwd(), "anggotas.json"), encoding="utf-8") as file:
        content = load(file)
        
    hari_ini = date.today().strftime("%Y-%m-%d")
    
    while True:
        try:
            id_baru = generate_idanggota()
            assert id_baru not in content
            break
        except AssertionError:
            continue
    
    content[id_baru] = {
            "idanggota" : id_baru,
            "nama"      : nama,
            "alamat"    : alamat,
            "tanggal"   : hari_ini,
            "telepon"   : f"+62{telp}"
    }
    
    with open("anggotas.json", "w") as file:
        dump(content, file, indent= 4)
        
    print("Data berhasil ditambahkan")
    input("Tekan enter untuk lanjut ")


# 2) B dan C
# Fungsi cari anggota
def cari_anggota_by_id(id_anggota):
    with open(path.join(getcwd(), "anggotas.json"), encoding="utf-8") as file:
        content = load(file)
    
    if id_anggota in content:
        return content[id_anggota]
    else:
        return {}

# Fungsi tampilkan anggota
def tampilkan_anggota(look):
    if look == {}:
        print("Tidak ada anggota !")
    else:
        id = look["idanggota"]
        nama = look["nama"]
        alamat = look["alamat"]
        telp = look["telepon"]
        tgl = look["tanggal"]
        
        print(f"""ID Anggota      : {id} 
Nama            : {nama}
Alamat          : {alamat} 
Telepon         : {telp}
Tanggal Daftar  : {tgl}""")
    
    input("Tekan enter untuk lanjut ")

# 2) D
# Fungsi mengedit anggota
from random import choices
from json import load,dump
from os import path, getcwd, system

def edit_anggota():
    while True:
        # Buka JSON 
        with open(path.join(getcwd(), "anggotas.json"), encoding="utf-8") as file:
            content = load(file)
        
        # Cari anggota by id
        dicari = input("Ketik ID anggota yang akan diedit : ")
        cari = cari_anggota_by_id(dicari)
        
        if cari == {}:
            print("Data anggota tidak ditemukan !")
            
            while True:
                try:
                    ulang = input("Cari lagi (Y/y = Ya, T/t = Tidak)?")
                    assert ulang.lower() in ["y", "t"], "Input tidak valid"
                    break
                except AssertionError as er:
                    print(er)
            
            if ulang.lower() == "y":
                system("cls")
            else:
                input("Tekan enter untuk kembali ke menu utama ")
                break
        else:
            id = cari["idanggota"]
            nama = cari["nama"]
            alamat = cari["alamat"]
            telepon = cari["telepon"]
            
            nama_baru = input(f"Nama : {nama} -> ")
            if nama_baru.strip() != "":
                cari["nama"] = nama_baru
                
            alamat_baru = input(f"Alamat : {alamat} -> ")
            if alamat_baru.strip() != "":
                cari["alamat"] = alamat_baru
                
            telepon_baru = input(f"Telepon : {telepon} -> ")
            if telepon_baru.strip() != "":
                cari["telepon"] = f"{telepon_baru}"
            
            content[id] = cari
            
            with open("anggotas.json", "w") as file:
                dump(content, file, indent= 4)
            
        break
