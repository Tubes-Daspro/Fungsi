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
    return AdminStatus

def Register(user):
    data = [0 for i in range(6)]
    if(AdminStatus):
        for i in range (6):
            if (i == 0):
                data[i] = input("Masukkan id: ")
            elif(i == 1):
                data[i] = input("Masukkan username: ")
            elif(i == 2):
                data[i] = input("Masukkan nama: ")
            elif (i == 3):
                data[i] = input("Masukkan alamat: ")
            elif (i == 4):
                data[i] = input("Masukkan password: ")
            else:
                data[i] = input("Masukkan role: ")
        user.append(data)
    else:
        print("Access Denied.")
    return user
