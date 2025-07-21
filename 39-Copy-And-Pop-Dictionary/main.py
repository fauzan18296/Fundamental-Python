# Copy Dictionary

teman_teman = {
  "cup" : "ucup surucup",
  "tong" : "otong surotong",
  "dung" : "dudung surudung",
  "sep" : "asep si kasyep",
  "cuy" : "ucuy surucuy",
}

friends = teman_teman.copy()

print(f"teman-teman : {teman_teman}\n")
print(f"friends : {friends}\n")

teman_teman["cup"] = "ucup si kweren"
print(f"teman-teman : {teman_teman}\n")
print(f"friends : {friends}\n")

# Pop Dictionary ( Data yang hilang akan berdasarkan key )
data_asep = friends.pop("sep")
print(f"data asep : {data_asep}\n")
print(f"friends : {friends}\n")

# Pop Item Dictionary ( Data yang hilang hanya data terakhir aja )
data_terakhir = friends.popitem()
print(f"data terakhir : {data_terakhir}\n")
print(f"friends : {friends}\n")