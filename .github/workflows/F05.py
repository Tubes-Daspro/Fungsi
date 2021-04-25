#Fungsi menambah item
def tambah_item(array_data):
    if(AdminStatus):
        i = 0
        check = False
        id_baru = input("Masukkan ID yang ingin ditambahkan: ")
        if(id_baru[0] == "G" and len(id_baru) >= 2):
            for array in array_data:
                if(array[0] == id_baru):
                    print("ID sudah ada.")
                    check = True
                    break
                elif(id_baru[1] != int):
                    print("Format ID Anda salah.")
                    check = True
                    break
            while(check == True):
                id_baru = input("Masukkan ID yang ingin ditambahkan: ")
                for array in array_data:
                    if(array[0] == id_baru):
                        print("ID sudah ada.")
                        i += 1
                if(i == 0):
                    check = False
            if(check == False):
                nama = input("Masukkan nama gadget Anda: ")
                deskripsi = input("Masukkan deskripsi: ")
                jumlah = int(input("Masukkan jumlah: "))
                rarity = input("Masukkan rarity item: ")
                tahun_ditemukan = int(input("Masukkan tahun ditemukan: "))
                array_baru = [id_baru, nama, deskripsi, jumlah, rarity, tahun_ditemukan]
                array_data.append(array_baru)
        elif(id_baru[0] == "C" and len(id_baru) >= 2):
            for array in array_data:
                if(array[0] == id_baru):
                    print("ID sudah ada.")
                    check = True
                    break
                elif(id_baru[1] != int):
                    print("Format ID Anda salah.")
                    check = True
                    break
            while(check == True):
                id_baru = input("Masukkan ID yang ingin ditambahkan: ")
                for array in array_data:
                    if(array[0] == id_baru):
                        print("ID sudah ada.")
                        i += 1
                if(i == 0):
                    check = False
            if(check == False):
                nama = input("Masukkan nama consumable Anda: ")
                deskripsi = input("Masukkan deskripsi: ")
                jumlah = int(input("Masukkan jumlah: "))
                rarity = input("Masukkan rarity item: ")
                array_baru = [id_baru, nama, deskripsi, jumlah, rarity]
                array_data.append(array_baru)
        else:
            print("ID yang dimasukkan invalid.")
    else:
        print("Access Denied.)
    return array_data
