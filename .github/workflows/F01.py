print("Hello, World!)
f = open("datacontoh.csv","r")
lines = f.readlines()
f.close()
print(lines)

f = open("datacontoh.csv","r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
for line in lines:
  print(line)

f = open("datacontoh.csv","r")
raw_lines = f.readlines()
f.close()
lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
def convert_line_to_data(line):
  raw_array_of_data = line.split(",")
  array_of_data = [data.strip() for data in raw_array_of_data]
  return array_of_data
def convert_array_data_to_real_values(array_data):
  arr_cpy = array_data[:]
  for i in range(3):
    if(i == 0):
      arr_cpy[i] = int(arr_cpy[i])
    elif(i == 2):
      arr_cpy[i] = float(arr_cpy[i])
  return arr_cpy
raw_header = lines.pop(0)
header = convert_line_to_data(raw_header)
print(header)
for line in lines:
  array_of_data = convert_line_to_data(line)
  real_values = convert_array_data_to_real_values(array_of_data)
  print(real_values)
