# F09 Mengembalikan Gadget  +  FB02 Mengembalikan Gadget secara Parsial

def kembalikan_gadget(data_gadget,data_gadget_borrow_history,data_gadget_return_history,id_user):
    # Mengembalikan data gadget dan data riwayat pengembalian gadget yang telah dimodifikasi
    # Return type : (array of array of string, array of array of string)

    # KAMUS LOKAL

    # VARIABEL

    # input_index_user_borrow_history : string    (input nomor gadget)
    # index_user_borrow_history : integer    (index user_borrow_history yang berdasarkan input_index_user_borrow_history)
    # input_jumlah_gadget_kembali : string    (input jumlah gadget yang akan dikembalikan)
    # jumlah_gadget_kembali : integer    (input jumlah gadget yang akan dikembalikan yang diubah menjadi integer)
    # tanggal_pengembalian : string    (input tanggal pengembalian)

    # user_gadget_borrow_history : array of [string,string,string,integer]    (menampung data gadget yang bisa dikembalikan oleh user)
    # id_gadget : string    (id gadget yang akan dikembalikan)
    # id_peminjaman : string    (id peminjaman gadget yang akan dikembalikan)
    # id_pengembalian : string    (id pengembalian yang akan menjadi data pada data_gadget_return_history)
    # id_peminjaman terakhir : string    (menyatakan id peminjaman terakhir dari gadget yang akan dikembalikan)
    # jumlah_gadget : integer    (menyatakan jumlah gadget yang bisa dikembalikan)
    # nama_gadget : integer    (menyatakan nama gadget yang bisa dikembalikan)
    # nama_gadget_found : boolean    (menyatakan bahwa nama gadget ditemukan)
    # sisa_pengembalian : integer    (menyatakan banyaknya gadget yang masih perlu dikembalikan)

    # skip_data : boolean    (menyatakan bahwa pemrosesan data bersangkutan harus dilewati)
    # data_found_in_return : boolean    (menyatakan bahwa data ditemukan di data_gadget_return_history)
    # index_borrow_history : integer    (counter untuk iterasi data_gadget_borrow_history)
    # index_gadget : integer    (counter untuk iterasi data_gadget)
    # index_peminjaman : integer    (counter untuk iterasi data_gadget_return_history)
    # i : integer    (counter untuk iterasi)

    # is_valid : boolean    (menyatakan apakah input yang dimasukkan oleh user valid)
    # is_operating : boolean    (menyatakan apakah program masih perlu berjalan)
    # exit_code : integer    (menyatakan penyebab terminasi berjalannya program)


    # FUNGSI
    # function is_date_valid(tanggal : string) -> boolean
    # { Mengembalikan True jika tanggal merupakan nilai yang valid. Tanggal merupakan nilai yang valid jika nilainya ada pada kalender }

    # ALGORITMA
    is_operating = True
    exit_code = 0
    is_valid = True

    # Menampilkan menu pengembalian gadget

    # Membuat list gadget yang sedang dipinjam user
    user_gadget_borrow_history = [] #[...[id_gadget,nama_gadget,id_peminjaman, jumlah_gadget]...]
    id_gadget = ''
    nama_gadget = ''
    id_peminjaman = ''
    jumlah_gadget = 0
    

    for index_borrow_history in range(len(data_gadget_borrow_history)-1, -1, -1):
        if data_gadget_borrow_history[index_borrow_history][1] == id_user:
            skip_data = False
            data_found_in_return = False
            index_return_history = len(data_gadget_return_history) - 1

            while (index_return_history >= 0):
                if data_gadget_borrow_history[index_borrow_history][0] == data_gadget_return_history[index_return_history][1]:
                    if data_gadget_return_history[index_return_history][4] > 0:
                        # Entry sudah dikembalikan, tapi baru sebagian
                        jumlah_gadget = data_gadget_return_history[index_return_history][4]
                        data_found_in_return = True
                        break
                    else:
                        # Entry sudah dikembalikan seluruhnya
                        skip_data = True
                        break
                index_return_history -= 1

            if not(data_found_in_return):
                # Entry belum dikembalikan sama sekali
                jumlah_gadget = data_gadget_borrow_history[index_borrow_history][4]

            id_gadget = data_gadget_borrow_history[index_borrow_history][2]
            id_peminjaman = data_gadget_borrow_history[index_borrow_history][0]

            # Pencarian nama gadget
            nama_gadget_found = False
            for index_gadget in range(len(data_gadget)):
                if data_gadget_borrow_history[index_borrow_history][2] == data_gadget[index_gadget][0]:
                    nama_gadget = data_gadget[index_gadget][1]
                    nama_gadget_found = True
            if not(nama_gadget_found):
                nama_gadget = "Informasi telah dihapus, namun gadget masih bisa dikembalikan."

            # Penambahan data ke user_gadget_borrow_history
            if not(skip_data):
                user_gadget_borrow_history.append([id_gadget,nama_gadget,id_peminjaman,jumlah_gadget])

    # Mengecek apakah user sedang meminjam suatu gadget
    if len(user_gadget_borrow_history) == 0:
        is_operating = False
        exit_code = 1

    if exit_code == 0:
        print("== DAFTAR ITEM YANG BISA DIKEMBALIKAN ==")
        # Menampilkan pilihan gadget yang dapat dikembalikan
        for i in range(len(user_gadget_borrow_history)):
            print(str(i+1) + ". " + user_gadget_borrow_history[i][1] + " (x" + str(user_gadget_borrow_history[i][3]) + ")")
    
    if is_operating:
        # Input ID gadget yang ingin dikembalikan
        input_index_user_borrow_history = input("Masukkan nomor gadget yang ingin dikembalikan (1 - " + str(len(user_gadget_borrow_history)) + ") : ")
    
        # Validasi input nomor gadget
        # Validasi input nomor gadget merupakan bilangan bulat positif

        for i in range(len(input_index_user_borrow_history)):
            if ord(input_index_user_borrow_history[i]) < 48 or ord(input_index_user_borrow_history[i]) > 57:
                is_valid = False

    # Validasi input nomor gadget sesuai rentang
    if is_valid and is_operating:
        index_user_borrow_history = int(input_index_user_borrow_history)
        index_user_borrow_history -= 1

        if index_user_borrow_history > len(user_gadget_borrow_history)-1:
            is_valid = False
    
    if not(is_valid):
        is_operating = False
        exit_code = 2


    # Input jumlah gadget bersangkutan yang ingin dikembalikan
    if is_valid and exit_code == 0:
        input_jumlah_gadget_kembali = input("Jumlah gadget yang ingin dikembalikan: ")

        # Validasi input jumlah gadget bersangkutan yang ingin dikembalikan
        for i in range(len(input_jumlah_gadget_kembali)):
            if ord(input_jumlah_gadget_kembali[i]) < 48 or ord(input_jumlah_gadget_kembali[i]) > 57:
                is_valid = False

    if not(is_valid) and is_operating:
        is_operating = False
        exit_code = 3

    # Validasi jumlah pengembalian tidak lebih dari jumlah gadget yang dipinjam
    if is_valid and exit_code == 0:
        jumlah_gadget_kembali = int(input_jumlah_gadget_kembali)
        if jumlah_gadget_kembali > user_gadget_borrow_history[index_user_borrow_history][3]:
            is_valid = False

    if not(is_valid) and is_operating:
        is_operating = False
        exit_code = 4

    if is_valid and exit_code == 0:
        # Input tanggal pengembalian
        tanggal_pengembalian = input("Tanggal pengembalian: ")

        # Validasi input tanggal peminjaman
        is_valid = is_date_valid(tanggal_pengembalian)

    if not(is_valid) and is_operating:
        is_operating = False
        exit_code = 5

    if is_valid and exit_code == 0:
        # Penentuan atribut sisa pengembalian
        sisa_pengembalian = user_gadget_borrow_history[index_user_borrow_history][3] - jumlah_gadget_kembali


        # Modifikasi atribut pada data gadget
        gadget_found = False
        index_gadget = -1
        while index_gadget < len(data_gadget)-1:
            index_gadget += 1
            if data_gadget[index_gadget][0] == user_gadget_borrow_history[index_user_borrow_history][0]:
                data_gadget[index_gadget][3] += jumlah_gadget_kembali
                gadget_found = True
                break

        if not(gadget_found):
            data_gadget[index_gadget] = ["", "", "", "", "", ""]


        # Penambahan data riwayat pengembalian gadget
        id_pengembalian = "GRH" + str(len(data_gadget_return_history) + 1)
        data_gadget_return_history.append([id_pengembalian,user_gadget_borrow_history[index_user_borrow_history][2],tanggal_pengembalian,jumlah_gadget_kembali,sisa_pengembalian])

        # Output
        print("\nItem " + user_gadget_borrow_history[index_user_borrow_history][1] + " (x" + str(jumlah_gadget_kembali) + ") berhasil dikembalikan!\n")

    if exit_code == 1:
        print("Anda tidak sedang meminjam gadget apapun. Silahkan pilih perintah yang lain.\n")
    elif exit_code == 2:
        print("Input tidak valid! Nomor gadget yang dimasukkan tidak sesuai rentang.\n")
    elif exit_code == 3:
        print("Input tidak valid! Jumlah gadget yang dikembalikan harus dalam bilangan bulat positif\n")
    elif exit_code == 4:
        print("Input tidak valid! Jumlah gadget yang ingin dikembalikan lebih besar dari jumlah gadget yang dipinjam!\n")
    elif exit_code == 5:
        print("Input tidak valid! Tanggal tidak sesuai format.\n")

    return (data_gadget,data_gadget_return_history)


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
                print(ord(tanggal[i]))
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
