def Register(user):
    if(AdminStatus):
        inputdata = [0 for i in range (6)]
        inputdata[0] = str(len(user))
        check = False
        for i in range(5):
            if   (i == 1):
                inputdata[i] = input("Masukkan nama Anda: ")
                inputdata[i] = inputdata[i].title()
            elif (i == 2):
                inputdata[i] = input("Masukkan username: ")
                for array_data in user:
                    if(array_data[i] == inputdata[i]):
                        print("Username sudah ada.")
                        check = True
                    break
                if(check):
                    break
            elif (i == 3):
                inputdata[i] = input("Masukkan password: ")
            elif (i == 4):
                inputdata[i] = input("Masukkan alamat: ")
            inputdata[5] = "User"
        if (check == False):
            user.append(inputdata)
    else:
        print("Access Denied.")
    return user
