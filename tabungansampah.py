from datetime import date
from random import choices
from json import load, dump
from os import path, getcwd, system

def input_of_options(prompt:str, ls_opt:list):
    while True:
        try:
            masuk = input(prompt)
            assert masuk.strip() in ls_opt, "Input tidak valid !"
            break
        except AssertionError as er:
            print(er)
    
    return masuk.strip()

def input_normal(prompt):
    while True:
        try:
            masuk = input(prompt)
            assert len(masuk.strip()) > 0, "Input tidak boleh kosong atau hanya spasi !"
            break
        except AssertionError as er:
            print(er)
    
    return masuk.strip()

def input_money_w_params(prompt:str, moneyparam:float):
    while True:
        try:
            amount = float(input(prompt))
            assert amount >= 0, "Uang tidak negatif!"
            assert amount % 100 == 0, "Uang harus dalam kelipatan 100 rupiah!"
            assert amount < 10_000_000, "Uang terlalu besar!"
            assert moneyparam - amount >= 0, "uang tidak cukup"
            break
        except ValueError:
            print("Masukkan uang dengan benar")
        except AssertionError as er:
            print(er)
    return amount

def generate_idtransaksi():
    ls_ap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ls_num = "0123456789"
    return ''.join(choices(ls_num, k=7))

def show_invoice1(idanggota):
    with open(path.join(getcwd(), "anggotas.json"), encoding="utf-8") as file:
        content = load(file)
        data = content[idanggota]
        
    print(f"""Penambahan Tabungan Sampah. 
Input ID Anggota : {idanggota} 
============================================= 
IDAnggota : {idanggota:<15} | Nama  : {data["nama"]} 
Telepon   : {data["telepon"]:<15} | Alamat: {data["alamat"]} 
============================================= 
--------------------------------------------- 
Kode    | Jenis Sampah  | Harga Satuan (Rp)     
--------------------------------------------- 
1       | Kardus        | 500      
2       | Botol plastic | 300 
3       | Logam besi    | 800 
4       | Tembaga       | 950 
---------------------------------------------""")

def show_invoice2(idanggota):
    with open(path.join(getcwd(), "anggotas.json"), encoding="utf-8") as file:
        content = load(file)
        data = content[idanggota]
        
    print(f"""Penambahan Tabungan Sampah. 
Input ID Anggota : {idanggota} 
============================================= 
IDAnggota : {idanggota:<15} | Nama  : {data["nama"]} 
Telepon   : {data["telepon"]:<15} | Alamat: {data["alamat"]} 
=============================================""")

# 4) A
def tambah_tabungan(idanggota, kode, kuantitas):
    with open(path.join(getcwd(), f"produksampah.json"), encoding="utf-8") as file:
        produk = load(file)
    
    while True:
        try:
            with open(path.join(getcwd(), f"tabungan{idanggota}.json"), encoding="utf-8") as file:
                riwayat = load(file)
        except FileNotFoundError:
            ct = []
            riwayat = []
            with open(path.join(getcwd(), f"tabungan{idanggota}.json"), "w") as file:
                dump(ct, file, indent= 4)
        
        if (kode, kuantitas) == (None, None):
            show_invoice1(idanggota)
            
            kode = input_of_options("Pilih jenis sampah     : ", ["1", "2", "3", "4"])
            
            while True:
                try:
                    kuantitas = float(input("Kuantitas sampah       : "))
                    break
                except ValueError:
                    print("Input tidak valid !")
        
        hari_ini = date.today().strftime("%Y-%m-%d")
        while True:
            try:
                id_tr = generate_idtransaksi()
                assert id_tr not in [ ele["idtransaksi"] for ele in riwayat ]
                break
            except AssertionError:
                continue
        
        nilaisatuan = produk[kode]["hargasatuan"]
        total = nilaisatuan*kuantitas
        saldo = total if len(riwayat) == 0 else (riwayat[-1]["saldo"] + total)
        
        ls_tr = {
                "tanggal"       : hari_ini,
                "idtransaksi"   : id_tr,
                "tipetransaksi" : "K",
                "sampah"        : kode,
                "kuantitas"     : kuantitas,
                "nilaisatuan"   : nilaisatuan,
                "total"         : total,
                "saldo"         : saldo
            }

        with open(path.join(getcwd(), f"tabungan{idanggota}.json"), "w") as file:
            riwayat.append(ls_tr)
            dump(riwayat, file, indent= 4)
        
        print("Pencatatan transaksi tabungan sampah berhasil.")

        ulang = input_of_options("Ada jenis sampah lain akan ditabung (Y/Y=Ya, T/t=Tidak) ? : ", ["y", "Y", "T", "t"])
        
        if ulang == "y" or ulang == "Y":
            system("cls")
            kode, kuantitas = None, None
            continue
        elif ulang == "t" or ulang == "T":
            break

# Fungsi menambah tabungan
def tarik_tabungan(idanggota):
    show_invoice2(idanggota)
    
    while True:
        with open(path.join(getcwd(), f"tabungan{idanggota}.json"), encoding="utf-8") as file:
            riwayat = load(file)
        
        saldo = riwayat[-1]["saldo"]
        print(f"Saldo saat ini adalah           : Rp{saldo:,.2f}")
        
        tarik = input_money_w_params("Masukkan banyak uang ditarik    : ", saldo)
        saldo -= tarik
        print(f"Sisa saldo adalah               : Rp{saldo:,.2f}")
        
        hari_ini = date.today().strftime("%Y-%m-%d")
        while True:
            try:
                id_tr = generate_idtransaksi()
                assert id_tr not in [ ele["idtransaksi"] for ele in riwayat ]
                break
            except AssertionError:
                continue
        
        ls_tr = {
                "tanggal"       : hari_ini,
                "idtransaksi"   : id_tr,
                "tipetransaksi" : "D",
                "total"         : -tarik,
                "saldo"         : saldo
            }
        
        with open(path.join(getcwd(), f"tabungan{idanggota}.json"), "w") as file:
            riwayat.append(ls_tr)
            dump(riwayat, file, indent= 4)
        
        print("Pencatatan transaksi tabungan sampah berhasil.")

        ulang = input_of_options("Ada jenis sampah lain akan ditabung (Y/Y=Ya, T/t=Tidak) ? : ", ["y", "Y", "T", "t"])
        
        if ulang == "y" or ulang == "Y":
            system("cls")
            continue
        elif ulang == "t" or ulang == "T":
            break

# Fungsi tampilkan tabungan
def tampilkan_tabungan(idanggota):
    show_invoice2(idanggota)

    with open(path.join(getcwd(), f"tabungan{idanggota}.json"), encoding="utf-8") as file:
        riwayat = load(file)

    tanggal = riwayat[-1]["tanggal"]
    kode = riwayat[-1]["idtransaksi"]
    jenis = riwayat[-1]["tipetransaksi"]
    total = f'{riwayat[-1]["total"]:,.2f}'
    saldo = f'{riwayat[-1]["saldo"]:,.2f}'
    
    print(f"""Tanggal Transaksi Terakhir  : {tanggal} 
Kode Transaksi Terakhir     : {kode} 
Jenis Transaksi Terakhir    : {"Tabungan" if jenis == "K" else "Penarikan"}
Nilai Transaksi Terakhir    : {total}
Saldo Tabungan              : {saldo}""")
    
    input("Tekan enter untuk melanjutkan")
