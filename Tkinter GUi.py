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