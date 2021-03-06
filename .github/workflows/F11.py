# F11 Melihat Riwayat Peminjaman Gadget
        
def lihat_riwayat_pinjam_gadget(data_gadget_borrow_history,data_gadget,data_user):
    # I.S. data_gadget_borrow_history, data_gadget, dan data_user terdefinisi 
    # F.S. Ditampilkan 5 buah data ID peminjaman gadget, nama pengambil, nama gadget, tanggal peminjaman, dan jumlah peminjaman jika memungkinkan.  
    # Data yang ditampilkan terurut secara descending berdasarkan tanggal peminjaman. 
    # User diberikan opsi untuk menampilkan 5 buah data lagi jika memungkinkan. 


    # KAMUS LOKAL

    # VARIABEL

    # list_index_tanggal : array of array of integer    (menyimpan indeks, tanggal, bulan dan tahun masing-masing data)
    # i : integer    (indeks data pada data_gadget_borrow_history)
    # dd : integer    (tanggal)
    # mm : integer    (bulan)
    # yyyy : integer    (tahun)
    
    # index_sorted : integer    (menyatakan sampai indeks apa list telah terurut)
    # is_sorted : boolean    (menyatakan apakah list telah terurut)
    # temp : array of integer    (menampung data sementara untuk keperluan sorting)

    # batas_bawah : integer    (menyatakan indeks bawah pada list_index_tanggal yang akan ditampilkan)
    # batas_atas : integer    (menyatakan indeks atas pada list_index_tanggal yang akan ditampilkan)
    # index_gadget : integer    (counter untuk iterasi data_gadget)
    # index_user : integer    (counter untuk iterasi data_user)
    # is_continue : boolean    (menyatakan apakah fungsi akan terus berjalan)
    # nama_pengambil : string    (nama pengambil yang akan ditampilkan)
    # nama_gadget : string    (nama gadget yang akan ditampilkan)
    # nama_gadget_found : boolean    (menyatakan apakah nama gadget ditemukan)

    # FUNGSI
    # function is_more_recent(d1 : array of integer,d2 : array of integer) -> boolean
    # {Mengembalikan True jika d1 menyatakan tanggal yang lebih baru dari d2}

    # ALGORITMA
    # Pembuatan list index dan tanggal
    list_index_tanggal = [0 for i in range(len(data_gadget_borrow_history))]
    for i in range(len(data_gadget_borrow_history)):
        dd = int(data_gadget_borrow_history[i][3][0] + data_gadget_borrow_history[i][3][1])
        mm = int(data_gadget_borrow_history[i][3][3] + data_gadget_borrow_history[i][3][4])
        yyyy = int(data_gadget_borrow_history[i][3][6] + data_gadget_borrow_history[i][3][7] + data_gadget_borrow_history[i][3][8] + data_gadget_borrow_history[i][3][9])
        list_index_tanggal[i] = [i,dd,mm,yyyy]

    # Sorting berdasarkan tanggal secara descending ( bubble sort )
    if len(list_index_tanggal) > 1:
        index_sorted = 0
        is_sorted = False
        while index_sorted <= len(list_index_tanggal)-1 and not(is_sorted):
            is_sorted = True
            for i in range(len(list_index_tanggal)-1, index_sorted, -1):
                if is_more_recent(list_index_tanggal[i], list_index_tanggal[i-1]):
                    temp = list_index_tanggal[i]
                    list_index_tanggal[i] = list_index_tanggal[i-1]
                    list_index_tanggal[i-1] = temp
                    is_sorted = False
                elif list_index_tanggal[i-1][1] == list_index_tanggal[i][1] and list_index_tanggal[i-1][2] == list_index_tanggal[i][2] and list_index_tanggal[i-1][3] == list_index_tanggal[i][3]:
                    if list_index_tanggal[i][0] < list_index_tanggal[i-1][0]:
                        temp = list_index_tanggal[i]
                        list_index_tanggal[i] = list_index_tanggal[i-1]
                        list_index_tanggal[i-1] = temp
                        is_sorted = False
            index_sorted += 1

    # Output
    batas_bawah = 0
    if len(list_index_tanggal) < 5:
        batas_atas = len(list_index_tanggal)
    else:
        batas_atas = 5

    is_continue = True
    if len(list_index_tanggal) > 0:
        print("=====Riwayat Peminjaman Gadget=====\n")
        while batas_atas <= len(list_index_tanggal) and is_continue:
            for i in range(batas_bawah, batas_atas):
                
                # Pencarian nama pengambil
                nama_pengambil = ''
                for index_user in range(len(data_user)):
                    if data_gadget_borrow_history[i][1] == data_user[index_user][0]:
                        nama_pengambil = data_user[index_user][2]

                # Pencarian nama gadget
                nama_gadget = ''
                nama_gadget_found = False
                for index_gadget in range(len(data_gadget)):
                    if data_gadget_borrow_history[i][2] == data_gadget[index_gadget][0]:
                        nama_gadget = data_gadget[index_gadget][1]
                        nama_gadget_found = True
                if not(nama_gadget_found):
                    nama_gadget = "Informasi telah dihapus."

                # Output
                print("ID Peminjaman      : " + data_gadget_borrow_history[list_index_tanggal[i][0]][0])
                print("Nama Pengambil     : " + nama_pengambil)
                print("Nama Gadget        : " + nama_gadget)
                print("Tanggal Peminjaman : " + data_gadget_borrow_history[list_index_tanggal[i][0]][3])
                print("Jumlah             : " + str(data_gadget_borrow_history[list_index_tanggal[i][0]][4]))
                print()

            # Opsi menampilkan lebih banyak data
            if batas_atas < len(list_index_tanggal):
                user_input = input("Apakah anda ingin menampilkan entry tambahan lagi? (Y/N) : ")
                if user_input == 'N':
                    is_continue = False
                elif user_input == 'Y':
                    batas_bawah += 5
                    if batas_bawah >= len(list_index_tanggal):
                        is_continue = False
                    elif len(list_index_tanggal) - batas_atas >= 5:
                        batas_atas += 5
                        print("\n\n")
                    else:
                        batas_atas = len(list_index_tanggal)
                        print("\n\n")
                else:
                    print("Input tidak valid! Proses diakhiri.\n")
                    is_continue = False
            else:
                print("Semua riwayat telah ditampilkan.\n")
                is_continue = False
    else:
        print("Belum ada riwayat peminjaman.\n")


def is_more_recent(d1,d2):
    # Mengembalikan True jika d1 menyatakan tanggal yang lebih baru dari d2
    # Return type : boolean

    # KAMUS LOKAL
    # result : boolean    (menampung hasil pemrosesan)

    # ALGORITMA
    result = True
    if d1[3] > d2[3]:
        result = True
    elif d1[3] < d2[3]:
        result = False
    else:
        if d1[2] > d2[2]:
            result = True
        elif d1[2] < d2[2]:
            result = False
        else:
            if d1[1] > d2[1]:
                result = True
            else:
                result = False
    
    return result
            
