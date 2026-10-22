import tkinter as tk
from tkinter import ttk

def hasil_prediksi():
    # Fungsi ini akan dijalankan saat tombol diklik dan mengubah label luaran
    label_hasil.config(text="Prediksi Prodi Pilihan: Teknologi Informasi")

  # Inisialisasi jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  
root.geometry("450x600")
root.resizable(False, False)

# 1. Label Judul Aplikasi
judul_label = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan", 
    font=("Helvetica", 16, "bold")
)
judul_label.pack(pady=20)    

# Frame untuk menampung input agar posisinya rapi
frame_input = ttk.LabelFrame(root, text=" Input Nilai Mata Pelajaran ")
frame_input.pack(pady=10, padx=20, fill="both", expand=True)

# List untuk menyimpan referensi objek entry (10 input nilai mata pelajaran)
entries = []

for i in range(1, 11):
    # Label untuk setiap mata pelajaran
    lbl = ttk.Label(frame_input, text=f"Nilai Mata Pelajaran {i}:", font=("Arial", 10))
    lbl.grid(row=i-1, column=0, sticky="w", padx=10, pady=5)