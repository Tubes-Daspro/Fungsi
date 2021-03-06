
import argparse
from os import system, name, path, makedirs

from F01 import register
from F02 import login
from F03 import carirarity
from F04 import caritahun
from F05 import tambah_item
from F06 import hapusitem
from F07 import ubah_jumlah
from F08 import pinjam_gadget
from F09 import kembalikan_gadget
from F10 import minta_consumable
from F11 import lihat_riwayat_pinjam_gadget
from F12 import lihat_riwayat_kembali_gadget
from F13 import lihat_riwayat_ambil_consumable
from F14 import load
from F15 import simpan
from F16 import help_awal, help_admin, help_user


# Loading data
parser = argparse.ArgumentParser()
parser.add_argument("folder")
args = parser.parse_args()

header_consumable_history, data_consumable_history = load(path.join(args.folder, "consumable_history.csv"), ";", [4])
header_consumable, data_consumable = load(path.join(args.folder, "consumable.csv"), ";", [3])
header_gadget_borrow_history, data_gadget_borrow_history = load(path.join(args.folder, "gadget_borrow_history.csv"), ";", [4])
header_gadget_return_history, data_gadget_return_history = load(path.join(args.folder, "gadget_return_history.csv"), ";", [3,4])
header_gadget, data_gadget = load(path.join(args.folder, "gadget.csv"), ";", [3,5])
header_user, data_user = load(path.join(args.folder, "user.csv"), ";", [])

print("Loading data...\n\n")

def simpan():
    folder = input("Masukkan nama folder penyimpanan: ")
    if not path.isdir(str(folder)):
        makedirs(folder)
    save(data_consumable, header_consumable, ";", path.join(folder, "consumable.csv"))
    save(data_consumable_history, header_consumable_history, ";", path.join(folder, "consumable_history.csv"))
    save(data_gadget, header_gadget, ";", path.join(folder, "gadget.csv"))
    save(data_user, header_user, ";", path.join(folder, "user.csv"))
    save(data_gadget_borrow_history, header_gadget_borrow_history, ";", path.join(folder, "gadget_borrow_history.csv"))
    save(data_gadget_return_history, header_gadget_return_history, ";", path.join(folder, "gadget_return_history.csv"))
    return

role = 0
status_login = 0
id_user = 0

while True:
    print()
    print("============Doremonangis Pouch of Pien=============")
    print()
    print("1. Login")
    print("2. Help")
    print("3. Exit")
    print()

    jawaban = input("Silahkan pilih (1 - 3): ")

    if jawaban == "1":
        role, status_login, id_user = login(data_user)
        if status_login :
            break
    elif jawaban == "2":
        while True:
            help_awal()
            x = input("Mengerti?(Y/N) ")
            if x == "Y" or x == "y":
                break
            elif x == "N" or x == "n":
                continue
            else :
                print("Saya anggap sudah mengerti.")
                break
    elif jawaban == "3":
        print("Terima kasih telah berkunjung!")
        break
    else :
        print("Input tidak valid!")

if role == "Admin":
    while True:
        print()
        print("============Doremonangis Pouch of Pien=============")
        print("========================Admin======================")
        print()
        print("1. Register")
        print("2. Pencarian Gadget Berdasarkan Rarity")
        print("3. Pencarian Gadget Berdasarkan Tahun Ditemukan")
        print("4. Menambah Item")
        print("5. Menghapus Gadget atau Consumable")
        print("6. Mengubah Jumlah Gadget atau Consumable pada Inventory")
        print("7. Melihat Riwayat Peminjaman Gadget")
        print("8. Melihat Riwayat Pengembalian Gadget")
        print("9. Melihat Riwayat Pengambilan Consumable")
        print("10. Save Data")
        print("11. Help")
        print("12. Exit")
        print()

        jawab = input("Silahkan pilih (1 - 12): ")

        if jawab == "1" :
            register(data_user)
        elif jawab == "2" :
            carirarity(data_gadget)
        elif jawab == "3" :
            caritahun(data_gadget)
        elif jawab == "4" :
            tambah_item(data_gadget, data_consumable)
        elif jawab == "5" :
            hapusitem(data_gadget,data_consumable)
        elif jawab == "6" :
            ubah_jumlah(data_gadget, data_consumable)
        elif jawab == "7" :
            lihat_riwayat_pinjam_gadget(data_gadget_borrow_history,data_gadget,data_user)
        elif jawab == "8" :
            lihat_riwayat_kembali_gadget(data_gadget_return_history,data_gadget_borrow_history,data_gadget,data_user)
        elif jawab == "9" :
            lihat_riwayat_ambil_consumable(data_consumable_history, data_consumable,data_user)
        elif jawab == "10" :
            x = input("Apakah anda yakin akan menyimpan perubahan?(Y/N) ")
            if x =="Y" or x == "y":    
                simpan()
                print("Perubahan berhasil disimpan.\n")
            elif x == "N" or x == "n":
                print("Perubahan tidak jadi disimpan.\n")
            else :
                print("Input tidak valid!\n")
        elif jawab == "11" :
            while True:
                help_admin()
                x = input("Mengerti?(Y/N) ")
                if x == "Y" or x == "y":
                    break
                elif x == "N" or x == "n":
                    continue
                else :
                    print("Saya anggap sudah mengerti.")
                    break
        elif jawab == "12" :
            jwb = input("Apakah Anda ingin menyimpan perubahan pada file?(Y/N) : ")
            if jwb == "Y" or jwb == "y":
                simpan()
                print("Terima kasih telah berkunjung!")
                break
            elif jwb == "N" or jwb == "n" :
                print("Tidak dilakukan penyimpanan file\n")
                print("Terima kasih telah berkunjung!")
                break
            else:
                print("Input tidak valid! Silahkan coba lagi")
        else :
            print("Input tidak valid! Silahkan coba lagi.")

elif role == "User":
    while True:
        print()
        print("============Doremonangis Pouch of Pien=============")
        print("========================User=======================")
        print()
        print("1. Pencarian Gadget Berdasarkan Rarity")
        print("2. Pencarian Gadget Berdasarkan Tahun Ditemukan")
        print("3. Meminjam Gadget")
        print("4. Mengembalikan Gadget")
        print("5. Meminta Consumable")
        print("6. Save Data")
        print("7. Help")
        print("8. Exit")
        print()

        jawab = input("Silahkan pilih (1 - 8): ")
        if jawab == "1" :
            carirarity(data_gadget)
        elif jawab == "2" :
            caritahun(data_gadget)
        elif jawab == "3":
            (data_gadget,data_gadget_borrow_history) = pinjam_gadget(data_gadget, data_gadget_borrow_history, data_gadget_return_history, id_user)
        elif jawab == "4" :
            (data_gadget, data_gadget_return_history) = kembalikan_gadget(data_gadget,data_gadget_borrow_history,data_gadget_return_history,id_user)
        elif jawab == "5" :
            (data_consumable, data_consumable_history) = minta_consumable(data_consumable,data_consumable_history,id_user)
        elif jawab == "6" :
            x = input("Apakah anda yakin akan menyimpan perubahan?(Y/N) ")
            if x =="Y" or x == "y":    
                simpan()
                print("Perubahan berhasil disimpan.\n")
            elif x == "N" or x == "n":
                print("Perubahan tidak jadi disimpan.\n")
            else :
                print("Input tidak valid!\n")
        elif jawab == "7" :
            while True:
                help_user()
                x = input("Mengerti?(Y/N) ")
                if x == "Y" or x == "y":
                    break
                elif x == "N" or x == "n":
                    continue
                else :
                    print("Saya anggap sudah mengerti.")
                    break
        elif jawab == "8" :
            jwb = input("Apakah Anda ingin menyimpan perubahan pada file?(Y/N) : ")
            if jwb == "Y" or jwb == "y":
                simpan()
                print("Perubahan berhasil disimpan.")
                print("Terima kasih telah berkunjung!")
                break
            elif jwb == "N" or jwb == "n" :
                print("Tidak dilakukan penyimpanan file\n")
                print("Terima kasih telah berkunjung!")
                break
            else:
                print("Input tidak valid! Silahkan coba lagi")
        else :
            print("Input tidak valid! Silahkan coba lagi.")
