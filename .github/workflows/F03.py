def carirarity():
    HasilPencarian = []
    while True:
        N = input("Masukkan rarity: ")
        if N == "S" or N == "A" or N == "B" or N == "C":
            for i in range(len(x)):
                for j in range(len(x[i])):
                    if x[i][j] == N:
                        HasilPencarian.append(x[i])
                    else:
                        continue
            
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
            
            else:
                print("Tidak ada gadget yang ditemukan.")
            break
        
        else:
            print("Masukkan invalid. Masukkan yang benar.")
            continue
