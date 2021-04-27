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
