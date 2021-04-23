def adminpool():
    global Admins
    Admins = []
    for i in range(len(user)):
        for j in range(len(user[i])):
            if j == 5:
                if user[i][j] == "Admin":
                    Admins.append(user[i])

def adminconfirm():
    for i in range(len(Admins)):
        for j in range(len(Admins[i])):
            if j == 1:
                if Admins[i][j] == username:
                    global AdminStatus
                    AdminStatus = True

def hapusitem():
    while True:
        if AdminStatus == True:
            removetarget = 0
            ID = input("Masukkan ID item: ")
            for i in range(len(gadget)):
                for j in range(len(gadget[i])):
                    if j == 0:
                        if gadget[i][j] == ID:
                            removetarget = gadget[i]
            
            for l in range(len(consumable)):
                for m in range(len(consumable[l])):
                    if m == 0:
                        if consumable[l][m] == ID:
                            removetarget = consumable[l]
            
            if removetarget != 0:
                ver = input("Apakah anda yakin ingin menghapus " + removetarget[1] + "? (Y/N) ")
                if ver == "Y":
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
