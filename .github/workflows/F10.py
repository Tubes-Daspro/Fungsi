# F10 Meminta Consumable

def minta_consumable(data_consumable,data_consumable_history,id_user):
    # Mengembalikan data consumable dan data riwayat permintaan consumable yang telah dimodifikasi
    # Return type : (array of [string, string, string, integer, char], array of [string, string, string, string, integer])
    
    # KAMUS LOKAL

    # VARIABEL
    # id_item : string    (input id item yang ingin diminta)
    # tanggal_permintaan : string    (input tanggal permintaan)
    # input_jumlah_permintaan : string    (input jumlah consumable yang diminta)
    # jumlah_permintaan : integer    (input jumlah permintaan yang diubah menjadi tipe integer)

    # index_item : integer    (counter untuk iterasi data_consumable)
    # i : integer    (counter untuk iterasi)
    # id_pengambilan : string    (id pengambilan yang akan menjadi data pada data_consumable_history)

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
    while index_item < len(data_consumable) and not(is_valid):
        if  data_consumable[index_item][0] == id_item:
            is_valid = True
        else:
            index_item += 1

    if not(is_valid):
        is_operating = False
        exit_code = 1

    # Input tanggal permintaan
    if is_valid:
        tanggal_permintaan = input("Tanggal permintaan (DD/MM/YYYY): ")

        # Validasi input tanggal permintaan
        is_valid = is_date_valid(tanggal_permintaan)

    if not(is_valid) and is_operating:
        is_operating = False
        exit_code = 2

    # Input jumlah permintaan
    if is_valid:
        input_jumlah_permintaan = input("Jumlah permintaan: ")

        # Validasi input jumlah permintaan

        # Validasi jumlah permintaan merupakan bilangan bulat positif
        for i in range(len(input_jumlah_permintaan)):
            if ord(input_jumlah_permintaan[i]) < 48 or ord(input_jumlah_permintaan[i]) > 57:
                is_valid = False
        
    if not(is_valid) and is_operating:
        is_operating = False
        exit_code = 3

    if is_valid:
    # Validasi jumlah pengambilan tidak melebihi stock yang ada
        jumlah_permintaan = int(input_jumlah_permintaan)
        if jumlah_permintaan > int(data_consumable[index_item][3]) or jumlah_permintaan <= 0:
            is_valid = False

    if not(is_valid) and is_operating:
        is_operating = False
        exit_code = 4
        
    if is_valid:
        # Modifikasi atribut jumlah pada data consumable
        data_consumable[index_item][3] = str( int(data_consumable[index_item][3]) - jumlah_permintaan)

        # Penambahan data riwayat pengambilan consumable
        id_pengambilan = "CH" + str(len(data_consumable_history) + 1)
        data_consumable_history.append([id_pengambilan,id_user,id_item,tanggal_permintaan,jumlah_permintaan])

        # Output
        print("\nItem " + data_consumable[index_item][1] + " (x" + str(jumlah_permintaan) + ") berhasil diminta!\n")
    
    if exit_code == 1:
        print("Input tidak valid! Item tidak tersedia!\n")
    elif exit_code == 2:
        print("Input tidak valid! Tanggal tidak sesuai format.\n")
    elif exit_code == 3:
        print("Input tidak valid! Jumlah pengambilan harus dalam bilangan bulat positif.\n")
    elif exit_code == 4:
        print("Input tidak valid! Jumlah pengambilan consumable tidak sesuai stock consumable!\n")

    return (data_consumable,data_consumable_history)


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

        
