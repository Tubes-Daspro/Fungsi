# F06 Menghapus Item dari Database

def hapusitem(gadget,consumable):
    # Menghapus item dari repository.
    # Output: deletion of array of [integer,string,string,integer,string,integer]

    # KAMUS LOKAL

    # VARIABEL
    # ID : string (Input berupa id dari barang yang akan di delete.)
    # ver : string (Verifikasi apakah benda akan benar dihapus.)
    # i : integer (Counter untuk iterasi.)
    # awal,akhir : integer (Identifier apakah telah terjadi perubahan pada size array.)

    # ALGORITMA
    while True:
        ID = input("Masukkan ID item: ")
        ver = ''
        if ID != '' and ID[0] == "G":
            awal = len(gadget)
            for i in range(len(gadget)):
                if gadget[i][0] == ID:
                    ver = input("Apakah anda yakin ingin menghapus " + gadget[i][1] + " ? (Y/N) ")
                    if ver == 'Y':
                        gadget.pop(i)
                        print("Item telah berhasil dihapus.")
                        break

                    elif ver == 'N':
                        print("Item tidak jadi dihapus.")
                        break

                    else:
                        ver = 'N'
                        print("Masukan salah, item tidak jadi dihapus.")
                        break
            
            akhir = len(gadget)
            if awal == akhir and ver != 'N':
                print("Tidak ada gadget yang memiliki ID tersebut.")
                break
            
            else:
                break
        
        elif ID != '' and ID[0] == 'C':
            awal = len(consumable)
            for i in range(len(consumable)):
                if consumable[i][0] == ID:
                    ver = input("Apakah anda yakin ingin menghapus " + consumable[i][1] + " ? (Y/N) ")
                    if ver == 'Y':
                        consumable.pop(i)
                        print("Item telah berhasil dihapus.")
                        break

                    elif ver == 'N':
                        print("Item tidak jadi dihapus.")
                        break

                    else:
                        ver = 'N'
                        print("Masukan salah, item tidak jadi dihapus.")
                        break
            
            akhir = len(consumable)
            if awal == akhir and ver != 'N':
                print("Tidak ada consumable yang memiliki ID tersebut.")
                break
            
            else:
                break

        else:
            print("Masukan ID tidak valid. Masukkan ulang.")
            continue
