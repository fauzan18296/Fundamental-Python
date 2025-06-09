data = "ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string

'''
      1. Dengan menggunakan single quote '...'
      2. Dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)
data = "Menggunakan double quote"
print(data)

print('"Halo apa kabar?"')
print("'Halo apa kabar?'")
print("ini adalah hari senin")

# 2. Menggunakan tanda \
# Membuat tanda ' menjadi string
print('Mari sholat jum\'at')
print('g\'day, isn\'t it?')

# Backlash
print("C:\\user\\Ucup")

# Tab
print("ucup\t\t\totong, semakin jauhan")

# Backspace
print("ucup \botong, jadi deketan")

# Newline
print("baris pertama.\nbaris kedua.") # LF => Line Feed -> Unix, Macos, Linux
print("baris pertama.\rbaris kedua.") # CR => Carriage Return -> Commodore, Acorn, Lisp
print("baris pertama.\r\nbaris kedua.") # CRLF => Line Feed Carriage Return -> Dipakai oleh windows

# 3. String literal atau raw

# hati-hati
print('C:\new folder') # Akan salah pathnya

# Menggunakan raw string
print(r'C:\new folder')

# Multiline literal string
print("""
Nama: Ucup
Kelas: 3 SD
""")

# Multiline literal string dan raw
print(r"""
  Nama: Ucup
  Kelas: 3 SD\new normal
  Website: www.ucup.com/newID
""")