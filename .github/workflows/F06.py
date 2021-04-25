# F06 Menghapus Item dari Database

def adminpool():
    # Mengumpulkan akun-akun yang statusnya administator.
    # Output: (array of [integer,string,string,string,string,string])

    # KAMUS LOKAL

    # VARIABEL
    # Admins : array (Berupa kumpulan akun-akun admin. Akan berubah menjadi variabel global)
    # i,j : integer (Counter untuk iterasi.)

    # ALGORITMA    
    global Admins
    Admins = []
    for i in range(len(user)):
        for j in range(len(user[i])):
            if j == 5:
                if user[i][j] == "Admin":
                    Admins.append(user[i])

def adminconfirm():
    # Mengecek apakah user yang logged in berupa admin atau tidak.
    # Output: bool

    # KAMUS LOKAL

    # VARIABEL
    # AdminStatus : bool (Status akun yang logged in apakah admin atau bukan. Akan berubah menjadi variabel global.)
    # i,j : integer (Counter untuk iterasi.)

    # ALGORITMA
    global AdminStatus
    AdminStatus = False
    for i in range(len(Admins)):
        for j in range(len(Admins[i])):
            if j == 1:
                if Admins[i][j] == username:
                    AdminStatus = True

def hapusitem():
    # Menghapus item dari repository.
    # Output: deletion of array of [integer,string,string,integer,string,integer]

    # KAMUS LOKAL

    # VARIABEL
    # ID : integer (Input berupa id dari barang yang akan di delete.)
    # removetarget : array (Array dari benda yang akan dihapus.)
    # ver : string (Verifikasi apakah benda akan benar dihapus.)
    # i,j,l,m,a,b,c,d : integer (Counter untuk iterasi.)

    # ALGORITMA
    while True:
        if AdminStatus == True:
            removetarget = 0
            ID = input("Masukkan ID item: ")
            for i in range(len(gadget)): # Penentuan target benda yang akan dihapus.
                for j in range(len(gadget[i])):
                    if j == 0:
                        if gadget[i][j] == ID:
                            removetarget = gadget[i]
            
            for l in range(len(consumable)):
                for m in range(len(consumable[l])):
                    if m == 0:
                        if consumable[l][m] == ID:
                            removetarget = consumable[l]
            
            if removetarget != 0: # Pengecekan apakah target terdapat di repository.
                ver = input("Apakah anda yakin ingin menghapus " + removetarget[1] + "? (Y/N) ") # Verifikasi apakah yakin atas penghapusan.
                if ver == "Y": # Penghapusan target.
                    for a in range(len(gadget)):
                        for b in range(len(gadget[a])):
                            if b == 0:
                                if gadget[a][b] == removetarget[0]:
                                    gadget.pop(a)
                                    print()
                                    print("Item telah berhasil dihapus dari database.")
                   
                    for c in range(len(consumable)):
                        for d in range(len(consumable[c])):
                            if d == 0:
                                if consumable[c][d] == removetarget[0]:
                                    consumable.pop(c)
                                    print()
                                    print("Item telah berhasil dihapus dari database.")

                    break
                                          
                elif ver == "N":
                    print()
                    print("Item tidak jadi dihapus.")
                    break
                
                else:
                    print()
                    print("Masukkan invalid. Item tidak jadi dihapus.")
                    break
            
            else:
                print()
                print("Tidak ada item dengan ID tersebut.")
                break

        elif AdminStatus == False:
            print("Access Denied")
            break

