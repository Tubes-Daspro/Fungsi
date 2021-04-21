def Register(user):
    data = [0 for i in range(4)]
    for i in range (4):
        if (i == 0):
            data[i] = input("Masukkan nama anda: ")
        elif(i == 1):
            data[i] = input("Masukkan username anda: ")
        elif(i == 2):
            data[i] = input("Masukkan password Anda: ")
        else:
            data[i] = input("Masukkan alamat anda: ")
    user.append(data)
