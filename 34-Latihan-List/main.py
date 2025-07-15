# program list buku
list_buku = []
while True:
  print("Masukan data buku")
  judul = input("Masukan judul buku\t : ")
  penulis = input("Masukan nama penulis\t : ")
  buku_baru = [judul, penulis]
  list_buku.append(buku_baru)

  print("\n\n", "="*10, "Data Buku", "="*10)
  for index,buku in enumerate(list_buku):
    print(f"{index + 1} | {buku[0]} | {buku[1]}")

  print("\n\n", "="*20)
  is_lanjut = input("Apakah dilanjutkan?(y/n)")

  if is_lanjut == 'n':
    break

print("PROGRAM SELESAI!!")