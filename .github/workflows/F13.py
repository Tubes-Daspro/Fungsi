# F13 Melihat Riwayat PengambilanConsumable

def lihat_riwayat_ambil_consumable(data_consumable_history, data_consumable,data_user):
    # I.S. data_consumable, data_consumable_history, dan data_user terdefinisi 
    # F.S. Ditampilkan 5 buah data ID pengambilan consumable, nama pengambil, nama consumable, tanggal pengambilan, dan jumlah pengambilan jika memungkinkan.  
    # Data yang ditampilkan terurut secara descending berdasarkan tanggal pengembalian. 
    # User diberikan opsi untuk menampilkan 5 buah data lagi jika memungkinkan. 

    
    # KAMUS LOKAL

    # VARIABEL

    # list_index_tanggal : array of array of integer    (menyimpan indeks, tanggal, bulan dan tahun masing-masing data)
    # i : integer    (indeks data pada data_consumable_history)
    # dd : integer    (tanggal)
    # mm : integer    (bulan)
    # yyyy : integer    (tahun)
    
    # index_sorted : integer    (menyatakan sampai indeks apa list telah terurut)
    # is_sorted : boolean    (menyatakan apakah list telah terurut)
    # temp : array of integer    (menampung data sementara untuk keperluan sorting)

    # batas_bawah : integer    (menyatakan indeks bawah pada list_index_tanggal yang akan ditampilkan)
    # batas_atas : integer    (menyatakan indeks atas pada list_index_tanggal yang akan ditampilkan)
    # index_consumable : integer   (counter untuk iterasi data_consumable)
    # index_user : integer    (counter untuk iterasi user_data)
    # is_continue : boolean    (menyatakan apakah fungsi akan terus berjalan)
    # nama_pengambil : string    (nama pengambil yang akan ditampilkan)
    # nama_consumable : string    (nama consumable yang akan ditampilkan)
    # nama_consumable_found : boolean    (menyatakan apakah nama consumable ditemukan)

    # FUNGSI
    # function is_more_recent(d1 : array of integer,d2 : array of integer) -> boolean
    # {Mengembalikan True jika d1 menyatakan tanggal yang lebih baru dari d2}

    # ALGORITMA
    # Pembuatan list index dan tanggal
    list_index_tanggal = [0 for i in range(len(data_consumable_history))]
    for i in range(len(data_consumable_history)):
        dd = int(data_consumable_history[i][3][0] + data_consumable_history[i][3][1])
        mm = int(data_consumable_history[i][3][3] + data_consumable_history[i][3][4])
        yyyy = int(data_consumable_history[i][3][6] + data_consumable_history[i][3][7] + data_consumable_history[i][3][8] + data_consumable_history[i][3][9])
        list_index_tanggal[i] = [i,dd,mm,yyyy]

    # Sorting berdasarkan tanggal secara descending (bubble sort)
    if len(list_index_tanggal) > 1:
        index_sorted = 0
        is_sorted = False
        while index_sorted <= len(list_index_tanggal)-1 and not(is_sorted):
            for i in range(len(list_index_tanggal)-1, index_sorted, -1):
                is_sorted = True
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

    if len(list_index_tanggal) > 0:
        print("=====Riwayat Permintaan Consumable=====\n")
        is_continue = True
        while batas_atas <= len(list_index_tanggal) and is_continue:
            for i in range(batas_bawah, batas_atas):
                
                # Pencarian nama pengambil
                nama_pengambil = ''
                for index_user in range(len(data_user)):
                    if data_consumable_history[i][1] == data_user[index_user][0]:
                        nama_pengambil = data_user[index_user][2]

                # Pencarian nama consumable
                nama_consumable = ''
                nama_consumable_found = False
                for index_consumable in range(len(data_consumable)):
                    if data_consumable_history[i][2] == data_consumable[index_consumable][0]:
                        nama_consumable = data_consumable[index_consumable][1]
                        nama_consumable_found = True
                if not(nama_consumable_found):
                    nama_consumable = "Informasi telah dihapus."

                # Output
                print("ID Pengambilan      : " + data_consumable_history[list_index_tanggal[i][0]][0])
                print("Nama Pengambil      : " + nama_pengambil)
                print("Nama Consumable     : " + nama_consumable)
                print("Tanggal Pengambilan : " + data_consumable_history[list_index_tanggal[i][0]][3])
                print("Jumlah              : " + str(data_consumable_history[list_index_tanggal[i][0]][4]))
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
        print("Belum ada riwayat permintaan. \n")


def is_more_recent(d1,d2):
    # Mengembalikan True jika d1 menyatakan tanggal yang lebih baru dari d2
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
