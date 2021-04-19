f = open("user.csv","r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
for line in lines:
    raw_array_of_data = line.split(",")
    array_of_data = [data.strip() for data in raw_array_of_data]
datas = []
for line in lines:
  datas.append(array_of_data)
array = [0 for i in range (4)]
for i in range(4):
    if  (i == 0):
        array[i] = input("Masukkan nama Anda: ")
    elif (i == 1):
        array[i] = input("Masukkan username: ")
    elif (i == 2):
        array[i] = input("Masukkan password: ")
    else:
        array[i] = input("Masukkan alamat: ")
datas.append(array)
print(datas)

def convert_datas_to_string():
  string_data = ",".join(array) + "\n"
  for arr_data in datas:
    arr_data_all_string = [str(var) for var in arr_data]
    string_data += ",".join(arr_data_all_string)
    string_data += "\n"
  return string_data
print()
print(convert_datas_to_string())

datas_as_string = convert_datas_to_string()
f = open("user.csv", "w")
f.write(datas_as_string)
f.close()
