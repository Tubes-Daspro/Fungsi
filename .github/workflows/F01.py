# def Register(user):
#         inputdata = [0 for i in range (6)]
#         inputdata[0] = str(len(user)+1)
#         check = False
#         for i in range(5):
#             if   (i == 1):
#                 inputdata[i] = input("Masukkan nama Anda: ")
#                 inputdata[i] = inputdata[i].title()
#             elif (i == 2):
#                 inputdata[i] = input("Masukkan username: ")
#                 for array_data in user:
#                     if(array_data[i] == inputdata[i]):
#                         print("Username sudah ada.")
#                         check = True
#                     break
#                 if(check):
#                     break
#             elif (i == 3):
#                 inputdata[i] = input("Masukkan password: ")
#             elif (i == 4):
#                 inputdata[i] = input("Masukkan alamat: ")
#             inputdata[5] = "User"
#         if (check == False):
#             user.append(inputdata)
#     return 

def register(data_user):
    data_baru = [0 for i in range(6)]
    data_baru[0] = str(len(data_user)+1)
    nama = input("Masukkan nama : ")
    data_baru[2] = nama.title()
    while True :
        data_baru[1] = input("Masukkan username : ")
        unik = True
        for i in range(len(data_user)):
            if data_baru[1] == data_user[i][1]:
                print("Username sudah ada.")
                unik = False
                break 
        if unik:
            break
    data_baru[3] = input("Masukkan alamat : ")
    data_baru[4] = input("Masukkan password : ")
    data_baru[5] = "User"
    data_user.append(data_baru)
    return
