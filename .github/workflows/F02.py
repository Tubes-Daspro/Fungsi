# def login(user):
#     username = input("Masukkan username: ")
#     password = input("Masukkan password: ")
#     find = False
#     for array_data in user:
#         i = 1
#         if (username == array_data[i]):
#             find = True
#             break
#     if(find == True):
#         i = 2
#         right_password = False
#         for array_data in user:
#             if(array_data[i] == password):
#                 right_password = True
#                 print("Anda berhasil masuk ke sistem!")
#                 right_username = username
#                 break
#         if(right_password == False):
#             print("Password yang Anda masukkan salah.")
#     else:
#         print("Username yang anda masukkan tidak terdaftar di sistem kami.")
#     return right_username

def login(user):
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    status_login = False
    for i in range(len(user)):
        if (username == user[i][1]):
            indeks = i
            status_login = True
            break
    if (status_login == True):
        password = hash_pass(password)
        if password == user[indeks][4]:
            role = user[indeks][5]
            id_user = user[indeks][0]
            print("halo", user[indeks][1] ,"! Anda berhasil masuk ke sistem! Selamat Datang!")
        else:
            status_login = False
            print("Password yang Anda masukkan salah.")
    else:
        print("Username yang anda masukkan tidak terdaftar di sistem kami.")
    return (role, status_login, id_user)

#Fungsi FB01 untuk keperluan Hashing password yang diinput user
def hash_pass(user_password):
    convert_password = hash(user_password)
    another_code = "gzA1bvGf"
    encode = (convert_password/1275) - 5766
    encode2 = hash(another_code)
    password = round(encode + encode2)
    while(password > 10**19 or password < 10**18):
        if(password < 10**18):
            validating_int = 3.67*(10**18)
            password += 3.67*(10**18)
            password = password/4
            password = round(password)
        else:
            password -= 6.43*(10**18)
    return password
