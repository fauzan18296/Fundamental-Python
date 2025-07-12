## Operasi

# index  0(-3)   1(-2)    2(-1)
data = ["Ucup", "Otong", "Dudung"]

# Mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

data_ucup = data[-3]
print(f"data ucup = {data_ucup}")

# Mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# Manipulasi data list
# Menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

data.insert(1, "asep")
print(f"data sesudah ditambah = \n{data}")

# Menambah di akhir list
data.append("Jajang")
print(f"data ditambah lagi = \n{data}")

# Menambah list dengan list 
data_baru = ["Ujang", "Usep", "Dadang"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# Merubah data
# kita ubah data 2 menjadi michael
data[2] = "Michael"
print(f"data rubah = \n{data}")

# Meremove data 
data.remove("Ujang")
print(f"data remove = {data}")
# data.remove("usep") => akan error karena huruf harus sesuai yaitu "Usep"

# Meremove data paling belakang
data_akhir = data.pop()
print(f"data akhir = \n{data}")
print(data_akhir)