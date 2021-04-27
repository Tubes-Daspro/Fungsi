def ubah_jumlah(array_data1, array_data2):
    id_item = input("Masukkan ID: ")
    operasi_jumlah = int(input("Masukkan jumlah: "))
    i = 0
    check = False
    for lines in array_data1:
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
    for lines in array_data2:
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
    if(check == False):
        print("Maaf ID yang Anda input tidak terdaftar di sistem.")
    return array_data1, array_data2
