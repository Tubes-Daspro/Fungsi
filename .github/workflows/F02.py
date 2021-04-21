def Login(user):
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    find = False
    for array_data in user:
        i = 0
        if (i == 0 and username == array_data[i]):
            find = True
            break
    if(find == True):
        i = 1
        right_password = False
        for array_data in user:
            if(array_data[i] == password):
                right_password = True
                print("Anda berhasil masuk ke sistem!")
                break
        if(right_password == False):
            print("Password yang Anda masukkan salah.")
    else:
        print("Username yang anda masukkan tidak terdaftar di sistem kami.")
