# Operator Dictionary

data_dict = {
  "cup" : "ucup surucup",
  "tong" : "otong surotong",
  "dung" : "dudung surudung",
}

# Panjang Dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary : {LENDICT}")

# Mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict : {CHECKKEY}")

# Mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis", "Key tidak ditemukan")) # Cek key dengan message tidak ditemukan

# Mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["sep"] = "asep si kasyep"
print(data_dict)

data_dict.update({"cup" : "ucup surucup"}) # kalau ada ya updatekan data tersebut
print(data_dict)
data_dict.update({"fauzan" : "fauzan kweren!!"}) # kalau ga ada data nya di add aja
print(data_dict)

# Mendelete data pada dictionary
del data_dict["fauzan"]
print(data_dict)