import datetime

data_waktu = datetime.datetime.now()
print(f"datetime now : {data_waktu}")
print(f"tahun : {data_waktu.year}")
print(f"hari : {data_waktu.strftime('%A')}")

from collections import Counter

data = ["a", "b", "c", "d", "a", "d", "e", "a"]
data_count = Counter(data)
print(f"data count = {data_count}")
print(f"jumlah a = {data_count['a']}")
print(f"jumlah d = {data_count['d']}")

# for count in data_count:
#   print(f"jumlah {count} = {data_count[count]}")
# for count in data_count.items():
#   print(f"jumlah {count}")

import io
file = io.open("file_text.txt", "r")
print(file.read())