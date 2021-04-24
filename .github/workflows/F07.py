def ubah_Jumlah(array_data):
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
    return array_data
