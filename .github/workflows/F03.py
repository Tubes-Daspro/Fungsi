# F03 Cari Rarity Gadget

def carirarity():
    # Mencari gadget yang rarity sama dengan rarity yang diinput.
    # Output: (array of [string,string,integer,string,integer])

    # KAMUS LOKAL

    # VARIABEL
    # R : string (Input rarity gadget yang akan dicari.)
    # i,j,a : integer (Counter untuk iterasi.)
    # HasilPencarian : Array (Array untuk menyimpan gadget-gadget yang raritynya sama dengan yang diinput di R.)
    
    # ALGORITMA    
    HasilPencarian = [] # Array yang mengumpulkan yang akan di output.
    while True: # While loop agar jika ada salah masukan akan mulai lagi dari awal tanpa ngecrash.
        R = input("Masukkan rarity: ")
        if R == "S" or R == "A" or R == "B" or R == "C": # Pengecekan apakah yang diinput berupa rarity yang valid.
            for i in range(len(gadget)): # Pengambilan gadget yang raritynya sama ke dalam array HasilPencarian.
                for j in range(len(gadget[i])):
                    if j == 4:
                        if gadget[i][j] == R:
                            HasilPencarian.append(gadget[i])

            print()
            print("Hasil pencarian:") # Output HasilPencarian.
            print()
            if len(HasilPencarian) != 0: # Pengecekan apakah HasilPencarian kosong atau tidak.
                for a in range(len(HasilPencarian)):
                    print("Nama             : ", HasilPencarian[a][1])
                    print("Deskripsi        : ", HasilPencarian[a][2])
                    print("Jumlah           : ", HasilPencarian[a][3])
                    print("Rarity           : ", HasilPencarian[a][4])
                    print("Tahun Ditemukan  : ", HasilPencarian[a][5])
                    print()
            
                break
            else:
                print("Tidak ada gadget yang ditemukan.")
            break
        
        else:
            print("Masukkan invalid. Masukkan yang benar.")
            continue
