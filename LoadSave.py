def ilangin_enter(data):
    for i in range(len(data)):
        data[i] = data[i].replace("\n", "")
    return data

def pisah(baris, pemisah):
    baris_baru =[""]
    j = 0
    for i in range(len(baris)):
        if baris[i] == pemisah:
            baris_baru.append("")
            j = j+1
        else :
            baris_baru[j] = baris_baru[j] + baris[i]
    return baris_baru

def ubah_string_ke_data(baris, pemisah):
    baris_baru1 = pisah(baris, pemisah)
    baris_baru2 = [data.strip() for data in baris_baru1]
    return baris_baru2

def ubah_tipe(datamentah, indeks_integer):
    data_baru = datamentah[:]
    for i in range(7):
        if i in indeks_integer and not (data_baru[i]==""):
            data_baru[i] = int(data_baru[i])
    return data_baru

def gabung_baris(datamentah):
    data = []
    for i in range(len(datamentah)):
        data.append(datamentah[i])
    return data


def load(file, pemisah, indeks_integer):
    f = open(file, "r")
    lines_mentah = f.readlines()
    f.close()
    lines = ilangin_enter(lines_mentah)
    header1 = lines.pop(0)
    header = ubah_string_ke_data(header1, pemisah)
    for i in range(len(lines)):
        lines[i] = ubah_string_ke_data(lines[i], pemisah)
        lines[i] = ubah_tipe(lines[i], indeks_integer)
    data = gabung_baris(lines)
    return (header, data)

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