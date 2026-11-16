# Python Dasar

Repositori ini berisi hasil praktikum **Belajar Python Dasar** dari Santrikoding. Setiap bab dikerjakan dengan contoh kode, dijalankan, didokumentasikan dengan screenshot, lalu di-commit dan di-push ke GitHub secara bertahap.

**Nama:** [Adi Hidayat]
**Kelas:** [XI RPL B]

## Ringkasan Materi

| Bab | Materi | Yang Dipelajari |
|---|---|---|
| 1 | Pengenalan dan Instalasi Python | Memasang Python, mengecek versi, REPL, dan membuat `hello.py` |
| 2 | Struktur Dasar Program | Komentar, indentasi, input dan output, serta fungsi `main` |
| 3 | Tipe Data Dasar | int, float, str, bool, list, tuple, dict, set, dan konversi tipe |
| 4 | Variable | Membuat variable, aturan penamaan, multiple assignment, `type()`, dan `del` |
| 5 | Konstanta | Konvensi penulisan, konstanta di dalam module, dan contoh pemakaian |
| 6 | Operator | Aritmatika, perbandingan, logika, penugasan, keanggotaan, dan identitas |
| 7 | Control Flow | `if`/`elif`/`else`, perulangan `for` dan `while`, serta `break` dan `continue` |
| 8 | Function | Parameter, `return`, default parameter, `*args`, dan `**kwargs` |
| 9 | List, Tuple, dan Set | Membuat, mengakses, mengubah, dan operasi himpunan |
| 10 | Dictionary | Membuat, mengakses, mengubah, menghapus, iterasi, dan nested dictionary |
| 11 | Class dan Object | Class, objek, constructor `__init__`, atribut, dan method |
| 12 | Encapsulation | Public, protected, private, getter, dan setter |
| 13 | Inheritance | Class induk dan turunan, method baru, dan `super()` |
| 14 | Polymorphism | Polymorphism pada method, inheritance, function, dan built-in function |
| 15 | Abstraction | Abstract class dengan modul `abc` |
| 16 | Exception Handling | `try`-`except`, `else`, `finally`, dan `raise` |
| 17 | File Handling | Membaca, menulis, menambah data, dan `with open` |
| 18 | Module | Membuat module, `import`, alias, `from ... import`, dan module `math` |
| 19 | Package | Struktur package, `__init__.py`, dan package bawaan Python |

## Struktur Folder

```
python-dasar/
├── my_package/         # Package contoh untuk bab 19
├── screenshots/        # Screenshot hasil eksekusi tiap program
├── *.py                # Contoh kode, diberi nama sesuai materi
├── requirements.txt
└── README.md
```

## Cara Menjalankan Program

1. Pastikan **Python** dan **Git** sudah terpasang.
2. Clone repositori ini:
   ```
   git clone https://github.com/adihidayat1710-svg/python-dasar.git
   cd python-dasar
   ```
3. Buat dan aktifkan virtual environment (Windows PowerShell):
   ```
   python -m venv venv
   venv\Scripts\Activate.ps1
   ```
4. Pasang dependensi:
   ```
   pip install -r requirements.txt
   ```
5. Jalankan salah satu program, contohnya:
   ```
   python hello.py
   ```

## Screenshot

Hasil eksekusi setiap program tersimpan di folder [`screenshots/`](screenshots/) dengan awalan nomor bab (misalnya `bab3_tipe_integer.png`).

## Alur Kerja Git

- Satu commit untuk setiap bab, dengan format `feat(babN): ...`.
- Setiap commit langsung di-push ke GitHub.
- Folder `venv/`, `__pycache__/`, dan file `.env` tidak ikut dilacak (lihat `.gitignore`).

## Catatan

Pada bab 16, file `exception_tanpa_handling.py` memang sengaja menghasilkan error `ZeroDivisionError`, untuk menunjukkan kenapa exception handling diperlukan.