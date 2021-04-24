def Login(user):
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    find = False
    for array_data in user:
        i = 1
        if (username == array_data[i]):
            find = True
            break
    if(find == True):
        i = 2
        right_password = False
        for array_data in user:
            if(array_data[i] == password):
                right_password = True
                print("Anda berhasil masuk ke sistem!")
                right_username = username
                break
        if(right_password == False):
            print("Password yang Anda masukkan salah.")
    else:
        print("Username yang anda masukkan tidak terdaftar di sistem kami.")
    return right_username
