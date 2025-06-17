# Operator dalam bentuk methods 

## Merubah case dari string 

# Merubah semua ke uppercase 

salam = "bro"
print('normal = ', salam)
salam = salam.upper()
print('upper = ', salam)

# Merubah semua ke lower case 
alay = "aKu Kece AbieeZZZZZzzzZ"
print("normal = ", alay)
alay = alay.lower()
print("lower = ", alay)

# Pengecekan dengan isX method 

## Contoh pengecekan lower case 
salam = "sist"
apakah_lower = salam.islower() # hasilnya akan bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya akan bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() -> Untuk mengecek semuanya huruf 
# isalnum() -> untuk mengecek huruf dan angka 
# isdecimal() -> untuk mengecek angka saja
# isspace() -> untuk mengecek spasi, tab, newline \n
# istitle() -> untuk mengecek semua kata yang dimulai dengan huruf besar

judul = "It Is Okay Not To Be Okay"
cek_judul = judul.istitle()
print(judul + " is title = " + str(cek_judul))

## Ngecek komponen startswith() endswith() -> keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = "+  str(cek_start))

cek_end = "Sarangae Chagia".endswith("Chagia")
print("end = "+  str(cek_end))

## Penggabungan komponen join(), split()
pisah = ['aku', 'sayang', 'kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = 'akuehmsayangehmkamu'
print(gabungan.split("ehm"))

## Alokasi karakter rjust(), ljust, center()
kanan = "kanan".rjust(10)
print("'" + kanan + "'")

kiri = "kiri".ljust(10)
print("'" + kiri + "'")

tengah = "tengah".center(20, "-")
print("'" + tengah + "'")

# Kebalikannya -> strip()
tengah = tengah.strip("-") # Menghilangkan tanda -
print("'" + tengah + "'")
