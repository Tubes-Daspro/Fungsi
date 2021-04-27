def tambah_item(array_data1, array_data2):
    count = 0
    check_count = 0
    array_checker = [0 for i in range (10)]
    for i in range (10):
        array_checker[i] = str(i)
    id_baru = input("Masukkan ID yang ingin ditambahkan: ")
    if(id_baru[0] == "G" and len(id_baru) >= 2):
        check = False
        while(check == False):
            found = False
            for array in array_data1:
                if(array[0] == id_baru):
                    print("ID sudah ada.")
                    found = True
                    id_baru = input("Masukkan ID yang ingin ditambahkan: ")
                    break
            if(found == False):
                for i in range (10):
                    if (array_checker[i] == id_baru[1]):
                        count = 1
                        break
            if(count == 0) and (found == False):
                print("ID yang dimasukkan invalid.")
                id_baru = input("Masukkan ID yang ingin ditambahkan: ")
            elif(count == 1):
                check = True
        if(count == 1):
            nama = input("Masukkan nama gadget Anda: ")
            deskripsi = input("Masukkan deskripsi: ")
            jumlah = int(input("Masukkan jumlah: "))
            rarity = input("Masukkan rarity item: ")
            tahun_ditemukan = int(input("Masukkan tahun ditemukan: "))
            array_baru = [id_baru, nama, deskripsi, jumlah, rarity, tahun_ditemukan]
            array_data1.append(array_baru)
    elif(id_baru[0] == "C" and len(id_baru) >= 2):
        check = False
        while(check == False):
            found = False
            for array in array_data2:
                if(array[0] == id_baru):
                    print("ID sudah ada.")
                    found = True
                    id_baru = input("Masukkan ID yang ingin ditambahkan: ")
                    break
            if(found == False):
                for i in range (10):
                    if (array_checker[i] == id_baru[1]):
                        count = 1
                        break
            if(count == 0) and (found == False):
                print("ID yang dimasukkan invalid.")
                id_baru = input("Masukkan ID yang ingin ditambahkan: ")
            elif(count == 1):
                check = True
        if(count == 1):
            nama = input("Masukkan nama consumable Anda: ")
            deskripsi = input("Masukkan deskripsi: ")
            jumlah = int(input("Masukkan jumlah: "))
            rarity = input("Masukkan rarity item: ")
            array_baru = [id_baru, nama, deskripsi, jumlah, rarity]
            array_data2.append(array_baru)
    else:
        print("ID yang dimasukkan invalid.")
    return array_data1, array_data2
