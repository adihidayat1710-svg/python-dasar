mahasiswa = {"nama": "Budi", "umur": 21, "jurusan": "Informatika", "angkatan": 2023}

mahasiswa.pop("jurusan")    # Menghapus dengan key
del mahasiswa["nama"]       # Menghapus dengan del

print(mahasiswa)