from os import system, name, path, makedirs

#SAVE
def ubah_ke_string(data, header, pemisah):
    data_baru = pemisah.join(header) + "\n"
    for item in data:
        data_baru2 = [str(var) for var in item]
        data_baru = data_baru + pemisah.join(data_baru2)
        data_baru = data_baru + "\n"
    return data_baru

def save(data, header, pemisah, file):
    f = open(file, "w")
    f.write(ubah_ke_string(data,header,pemisah))
    f.close()
    return

def simpan():
    folder = input("Masukkan nama folder penyimpanan: ")
    if not path.isdir(str(folder)):
        makedirs(folder)
    save(data_consumable, header_consumable, ";", path.join(folder, "consumable.csv"))
    save(data_consumable_history, header_consumable_history, ";", path.join(folder, "consumable_history.csv"))
    save(data_gadget, header_gadget, ";", path.join(folder, "gadget.csv"))
    save(data_user, header_user, ";", path.join(folder, "user.csv"))
    save(data_gadget_borrow_history, header_gadget_borrow_history, ";", path.join(folder, "gadget_borrow_history.csv"))
    save(data_gadget_return_history, header_gadget_return_history, ";", path.join(folder, "gadget_return_history.csv"))
    return
