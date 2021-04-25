def Register(user):
    data = [0 for i in range(6)]
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
    return user
