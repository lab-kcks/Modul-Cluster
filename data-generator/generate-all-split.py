import importlib

# filenames
files = [
    'generate-kota',
    'generate-siswa',
    'generate-mata-pelajaran',
    'generate-soal',
    'generate-jawaban-split',
]

# execute each file (pake importlib)
for file in files:
    importlib.import_module(file)
