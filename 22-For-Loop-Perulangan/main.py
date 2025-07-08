# Perulangan (loop)

# for kondisi:
#   aksi

# Ini dengan list
angka_2_list = [0, 2, 4, 8, 10] # Ini adalah list
print(angka_2_list)

for i in angka_2_list:
  print(f"i sekarang -> {i}")
  
print("akhir dari program 1 \n")

# Ini dengan range 
angka_2_range = range(5)
for i in angka_2_range:
  print(f"i sekarang -> {i}")
  
print("akhir dari program 2 \n")

angka_2_range = range(1, 5)
for i in angka_2_range:
  # print(f"i sekarang -> {i}")
  print("saya keren")
  
print("akhir dari program 3")

# menggunakan string 
data_str = "saya ganteng abiess"
for huruf in data_str:
  print(huruf)
  
print("akhir dari program 4 \n")
