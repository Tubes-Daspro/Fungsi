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

#Fungsi Utamanya yang di bawah itu yang di atas catatan aja biar gw kmrn kebayang codingnya gimana rightt
def ubah_Jumlah(array_data):
    if(AdminStatus):
        id_item = input("Masukkan ID: ")
        operasi_jumlah = int(input("Masukkan jumlah: "))
        i = 0
        check = False
        for lines in array_data:
            if(lines[i] == id_item):
                check = True
                if(operasi_jumlah < 0):
                    check_validasi = lines[3] + operasi_jumlah
                    if(check_validasi < 0):
                        print("Jumlah dari barang tersebut kurang.")
                    else:
                        lines[3] = check_validasi
                else:
                    lines[3] = lines[3] + operasi_jumlah
            else:
                continue
        if not (check):
            print("Maaf ID yang Anda input tidak terdaftar di sistem.")
    else:
        print("Access Denied.")
    return array_data
