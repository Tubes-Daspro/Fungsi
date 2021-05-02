# F08 Meminjam Gadget

def pinjam_gadget(data_gadget, data_gadget_borrow_history, data_gadget_return_history, id_user):
    # Mengembalikan data gadget dan data riwayat peminjaman gadget yang telah dimodifikasi
    # Return type : (array of [string,string,string,integer,char,integer], array of [string,string,string,string,integer])

    # KAMUS LOKAL

    # VARIABEL
    # id_item : string    (input id item yang ingin dipinjam)
    # tanggal peminjaman : string    (input tanggal peminjaman)
    # input_jumlah_peminjaman : string    (input jumlah gadget yang ingin dipinjam)
    # jumlah_peminjaman : integer    (input jumlah peminjaman yang diubah tipenya menjadi integer)

    # id_peminjaman : string    (id peminjaman yang akan menjadi data dalam data_gadget_borrow_history)
    # id_peminjaman_terakhir : string    (id peminjaman terakhir terhadap gadget yang sama sebelum peminjaman ini)
    # index_item : integer    (counter untuk iterasi array data_gadget)
    # index_peminjaman : integer    (counter untuk iterasi data_gadget_borrow_history)
    # index_pengembalian : integer    (counter untuk iterasi data_gadget_return_history)
    # i : integer    (counter untuk iterasi)
    # id_peminjaman_terakhir_found : boolean    (menyatakan apakah ada entry peminjaman item yang sama sebelumnya)
    # index_pengembalian_found : boolean    (menyatakan apakah ada entry pengembalian item dengan id_peminjaman_terakhir)

    # is_valid : boolean    (menyatakan apakah input yang dimasukkan oleh user valid)
    # is_operating : boolean    (menyatakan apakah program masih perlu berjalan)
    # exit_code : integer    (menyatakan penyebab terminasi berjalannya program)


    # FUNGSI
    # function is_date_valid(tanggal : string) -> boolean
    # { Mengembalikan True jika tanggal merupakan nilai yang valid. Tanggal merupakan nilai yang valid jika nilainya ada pada kalender }
    
    # ALGORITMA
    is_operating = True
    exit_code = 0

    # Input id item
    id_item = input("Masukan ID item: ")

    # Validasi input id item
    is_valid = False
    index_item = 0
    while index_item < len(data_gadget) and not(is_valid):
        if data_gadget[index_item][0] == id_item:
            is_valid = True
        else:
            index_item += 1

    if not(is_valid):
        is_operating = False
        exit_code = 1


    # Validasi user tidak sedang meminjam gadget yang sama
    if is_valid:
        # Pengecekan pernah adanya peminjaman oleh user terhadap gadget yang dipilih
        index_peminjaman = len(data_gadget_borrow_history) - 1 
        id_peminjaman_terakhir = ''
        id_peminjaman_terakhir_found = False
        while index_peminjaman >= 0 and not(id_peminjaman_terakhir_found):
            if data_gadget_borrow_history[index_peminjaman][1] == id_user and data_gadget_borrow_history[index_peminjaman][2] == id_item:
                id_peminjaman_terakhir_found = True
                id_peminjaman_terakhir = data_gadget_borrow_history[index_peminjaman][0]
            else:
                index_peminjaman -= 1

        # Bila pernah meminjam gadget yang dipilih, dilakukan pengecekan apakah gadget telah dikembalikan sepenuhnya
        if id_peminjaman_terakhir_found:
            index_pengembalian_found = False
            index_pengembalian = len(data_gadget_return_history) - 1
            while index_pengembalian >= 0 and not(index_pengembalian_found):
                if data_gadget_return_history[index_pengembalian][1] == id_peminjaman_terakhir:
                    index_pengembalian_found = True
                    if data_gadget_return_history[index_pengembalian][4] != 0:
                        is_valid = False
                index_pengembalian -= 1
            if not(index_pengembalian_found):
                is_valid = False


    if not(is_valid) and is_operating:
        is_operating = False
        exit_code = 2
        
    if is_valid:
        # Input tanggal peminjaman
        tanggal_peminjaman = input("Tanggal peminjaman (DD/MM/YYYY): ")

        # Validasi input tanggal peminjaman
        is_valid = is_date_valid(tanggal_peminjaman)

    if not(is_valid) and is_operating:
        is_operating = False
        exit_code = 3

    if is_valid:
        # Input jumlah peminjaman
        input_jumlah_peminjaman = input("Jumlah peminjaman: ")

        # Validasi jumlah peminjaman merupakan bilangan bulat
        for i in range(len(input_jumlah_peminjaman)):
            if ord(input_jumlah_peminjaman[i]) < 48 or ord(input_jumlah_peminjaman[i]) > 57:
                is_valid = False

    if not(is_valid) and is_operating:
        is_operating = False
        exit_code = 4


    if is_valid:
        # Validasi jumlah peminjaman tidak melebihi stock yang ada
        jumlah_peminjaman = int(input_jumlah_peminjaman)
        if jumlah_peminjaman > data_gadget[index_item][3] or jumlah_peminjaman <= 0:
            is_valid = False

    if not(is_valid) and is_operating:
        is_operating = False
        exit_code = 5
        
    if is_valid:
        # Modifikasi atribut jumlah pada data gadget
        data_gadget[index_item][3] = int(data_gadget[index_item][3]) - int(jumlah_peminjaman) 

        # Penambahan data riwayat peminjaman gadget
        id_peminjaman = "GBH" + str(len(data_gadget_borrow_history) + 1)
        data_gadget_borrow_history.append([id_peminjaman,id_user,id_item,tanggal_peminjaman,jumlah_peminjaman])

        # Output
        print("\nItem " + data_gadget[index_item][1] + " (x" + str(jumlah_peminjaman) + ") berhasil dipinjam!")
        print("ID peminjaman : " + id_peminjaman + "\n")
    
    if exit_code == 1:
        print("Input tidak valid! Item tidak tersedia!\n")
    elif exit_code == 2:
        print("Input tidak valid! Anda sedang meminjam gadget tersebut!\n")
    elif exit_code == 3:
        print("Input tidak valid! Tanggal tidak sesuai format.\n")
    elif exit_code == 4:
        print("Input tidak valid! Jumlah peminjaman harus dalam bilangan bulat positif\n")
    elif exit_code == 5:
        print("Input tidak valid! Jumlah peminjaman gadget tidak sesuai stock gadget!\n")

    return (data_gadget,data_gadget_borrow_history)


def is_date_valid(tanggal):
    # Mengembalikan True jika tanggal merupakan nilai yang valid.
    # Tanggal merupakan nilai yang valid jika nilainya ada pada kalender
    # Return type : boolean

    # KAMUS LOKAL
    # tanggal : string
    # dd,mm,yy : integer    {menyatakan tanggal, bulan, dan tahun pada tanggal}
    # is_kabisat : boolean  {menyatakan apakah yy menyatakan nilai tahun kabisat}

    # ALGORITMA
    # Pengecekan panjang string tanggal
    if len(tanggal) != 10:
        return False

    # Pengecekan kesesuaian tipe karakter pada string tanggal
    for i in range(10):
        if i == 2 or i == 5:
            if tanggal[i] != '/':
                return False
        else:
            if ord(tanggal[i]) < 48 and ord(tanggal[i]) > 57:
                return False

    # Pengecekan kevalidan nilai tanggal
    dd = int(tanggal[0] + tanggal[1])
    mm = int(tanggal[3] + tanggal[4])
    yy = int(tanggal[6] + tanggal[7] + tanggal[8] + tanggal[9])
    is_kabisat = (yy % 400 == 0) or (yy % 100 != 0 and yy % 4 == 0)

    if mm <= 12:
        if (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12) and dd <= 31 :
            return True
        elif (mm == 4 or mm == 6 or mm == 9 or mm == 11) and dd <= 30:
            return True
        elif mm == 2:
            if is_kabisat and dd <= 29:
                return True
            elif not(is_kabisat) and dd <= 28:
                return True
            else:
                return False
        else: 
            return False
    else:
        return False

