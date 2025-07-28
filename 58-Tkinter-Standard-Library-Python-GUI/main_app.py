# GUI -> Graphical User Interface
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init
window = tk.Tk()
window.configure(bg="black")
window.geometry("1000x500")
window.resizable(False, False)
window.title("Sapa Dia!")

# Variabel Dan Fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
  '''Fungsi ini akan dipanggil oleh tombol'''
  pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}"
  showinfo(title="Whazzup!", message=pesan)

# Frame Input
input_frame = ttk.Frame(window)
# Penempatan Grid, Pack, Place
input_frame.pack(padx=10, pady=10, fill='x', expand=True)

# Komponen-Komponen
# 1. Label untuk nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan: ", width=30)
nama_depan_label.pack(padx=10, fill='x', expand=True)
# 2. Entry Nama Depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN, width=30)
nama_depan_entry.pack(padx=10, fill='x', expand=True)
# 3. Label untuk nama belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang: ", width=30)
nama_belakang_label.pack(padx=10, fill='x', expand=True)
# 4. Entry Nama Belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG, width=30)
nama_belakang_entry.pack(padx=10, fill='x', expand=True)
# 5. Tombol
tombol_sapa = ttk.Button(input_frame, text="Sapa!", command=tombol_click, width=30)
tombol_sapa.pack(padx=10, pady=10,fill="x", expand=True)

# Main Loop Window
window.mainloop()