# F04 Cari Gadget Berdasarkan Tahun Ditemukan

def caritahun(gadget):
    # Mencari gadget yang tahun ditemukannya yang cocok dengan spesifikasi tahun yang diinput.
    # Output: (array of [string,string,integer,string,integer])

    # KAMUS LOKAL

    # VARIABEL
    # Thn : integer (Input tahun ditemukannya gadget yang akan dicari.)
    # Kateg : string (Input spesifikasi terhadap tahun input (lebih besar, lebih kecil, sama dengan, dll.))
    # i,j,a : integer (Counter untuk iterasi.)
    # HasilPencarian : Array (Array untuk menyimpan gadget yang tahun ditemukannya cocok dengan spesifikasi input.)
    
    # ALGORITMA    
    HasilPencarian = [] # Array yang mengumpulkan yang akan di output.
    while True:
        try: # Pengecekan apakah tahun yang dimasukkan berupa integer.
            Thn = int(input("Masukkan Tahun: "))
        except ValueError:
            print("Masukkan invalid. Masukkan yang benar.")
            continue

        Kateg = input("Masukkan kategori: ")
        if Kateg == ">" or Kateg == "<" or Kateg == ">=" or Kateg == "<=" or Kateg == "=": # Pengecekan apakah input berupa kategori valid.
            for i in range(len(gadget)):
                for j in range(len(gadget[i])):
                    if j == 5 and Kateg == ">": # Pengelompokkan gadget berdasarkan spesifikasi yang diinput.
                        if Thn > int(gadget[i][j]):
                            HasilPencarian.append(gadget[i])
                    elif j == 5 and Kateg == "<":
                        if Thn < int(gadget[i][j]):
                            HasilPencarian.append(gadget[i])
                    elif j == 5 and Kateg == ">=":
                        if Thn >= int(gadget[i][j]):
                            HasilPencarian.append(gadget[i])
                    elif j == 5 and Kateg == "<=":
                        if Thn <= int(gadget[i][j]):
                            HasilPencarian.append(gadget[i])
                    elif j == 5 and Kateg == "=":
                        if Thn == int(gadget[i][j]):
                            HasilPencarian.append(gadget[i])
                    
            print()
            print("Hasil pencarian:")
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
            print("Masukkan invalid. Masukkan yang benar")
            continue
