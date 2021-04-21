f = open("Book1.csv", "r")
barisdata = f.readlines()
f.close()
user = []
barisan = [isi.replace("\n", " ") for isi in barisdata]
print(barisan)
def changeCSV(baris):
    arraybaru = baris.split(",")
    arraykedua = [data.strip() for data in arraybaru]
    return arraykedua

awal = barisan.pop(0)
ubah = changeCSV(awal)

for line in barisan:
    databaru = changeCSV(line)
    user.append(databaru)

inputdata = [0 for i in range (4)]
for i in range(4):
    if   (i == 0):
        inputdata[i] = input("Masukkan nama Anda: ")
    elif (i == 1):
        inputdata[i] = input("Masukkan username: ")
    elif (i == 2):
        inputdata[i] = input("Masukkan password: ")
    else:
        inputdata[i] = input("Masukkan alamat: ")
user.append(inputdata)

def changeType():
    stringbaru = ",".join(ubah)
    for barisandata2 in user:
        stringbaru += ",".join(barisandata2)
        stringbaru += "\n"
    return stringbaru

newstring = changeType()

f = open("Book1.csv", "w")
f.write(newstring)
f.close()
