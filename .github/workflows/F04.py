def caritahun():
    HasilPencarian = []
    while True:
        try:
            Thn = int(input("Masukkan Tahun: "))
        except ValueError:
            print("Masukkan invalid. Masukkan yang benar.")
            continue

        Kateg = input("Masukkan kategori: ")
        if Kateg == ">" or Kateg == "<" or Kateg == ">=" or Kateg == "<=" or Kateg == "=":
            for i in range(len(x)):
                for j in range(len(x[i])):
                    if j == 4 and Kateg == ">":
                        if Thn > int(x[i][j]):
                            HasilPencarian.append(x[i])
                    elif j == 4 and Kateg == "<":
                        if Thn < int(x[i][j]):
                            HasilPencarian.append(x[i])
                    elif j == 4 and Kateg == ">=":
                        if Thn >= int(x[i][j]):
                            HasilPencarian.append(x[i])
                    elif j == 4 and Kateg == "<=":
                        if Thn <= int(x[i][j]):
                            HasilPencarian.append(x[i])
                    elif j == 4 and Kateg == "=":
                        if Thn == int(x[i][j]):
                            HasilPencarian.append(x[i])
                    
            print()
            print("Hasil pencarian:")
            print()
            if len(HasilPencarian) != 0:
                for a in range(len(HasilPencarian)):
                    for b in range(len(HasilPencarian[a])):
                        if b == 0:
                            print("Nama             : ",(HasilPencarian[a][b]))
                        elif b == 1:
                            print("Deskripsi        : ",(HasilPencarian[a][b]))
                        elif b == 2:
                            print("Jumlah           : ",(HasilPencarian[a][b]), " buah")
                        elif b == 3:
                            print("Rarity           : ",(HasilPencarian[a][b]))
                        elif b == 4:
                            print("Tahun Ditemukan  : ",(HasilPencarian[a][b]))
                        print()

                break    
            else:
                print("Tidak ada gadget yang ditemukan.")
                break
        else:
            print("Masukkan invalid. Masukkan yang benar")
            continue
