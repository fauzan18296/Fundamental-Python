''' Type hints untuk fungsi '''

# Bentuk standar fungsi yang udah kita pelajari

'''
Studi kasus
def fungsi(parameter):
  hasil = parameter ** 2
  print(hasil)
fungsi(1)
fungsi("Ucup")
fungsi(True)
'''

# Penggunaan type hints

import string

def sepuluh_pangkat(argument:int) -> int: # type integer dengan -> atau return integer
  '''Fungsi dengan hints'''
  output = 10 ** argument
  return output
HASIL = sepuluh_pangkat(2)
print(HASIL)

def display(argument: string):
  print(type(argument))
display("Ucup")