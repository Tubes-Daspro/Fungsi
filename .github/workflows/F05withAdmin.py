def adminpool():
    global Admins
    Admins = []
    for i in range(len(user)):
        for j in range(len(user[i])):
            if j == 5:
                if user[i][j] == "Admin":
                    Admins.append(user[i])

def adminconfirm():
    for i in range(len(Admins)):
        for j in range(len(Admins[i])):
            if j == 1:
                if Admins[i][j] == username:
                    global AdminStatus
                    AdminStatus = True
    return AdminStatus

def tambah_item(array_data):
    if(AdminStatus):
        id_baru = input("Masukkan ID yang ingin ditambahkan: ")
        if(id_baru[0] == "G"):
            nama = input("Masukkan nama Anda: ")
            deskripsi = input("Masukkan deskripsi: ")
            jumlah = int(input("Masukkan jumlah: "))
            rarity = input("Masukkan rarity item: ")
            tahun_ditemukan = input("Masukkan tahun ditemukan: ")
            array_baru = [id_baru, nama, deskripsi, jumlah, rarity, tahun_ditemukan]
            array_data.append(array_baru)
        elif(id_baru[0] == "C"):
            nama = input("Masukkan nama Anda: ")
            deskripsi = input("Masukkan deskripsi: ")
            jumlah = int(input("Masukkan jumlah:"))
            rarity = input("Masukkan rarity item: ")
            array_baru = [id_baru, nama, deskripsi, jumlah, rarity]
            array_data.append(array_baru)
        else:
            print("ID yang dimasukkan invalid.")
    else:
        print("Access Denied.")
    return array_data
