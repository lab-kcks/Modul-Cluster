from faker import Faker
import csv
import config
import json

fake = Faker()

total_siswa = config.total_siswa
total_soal = config.total_soal
id = 0

f = open("csv/jawaban.csv", "w")
writer = csv.writer(f, doublequote=True, quoting=csv.QUOTE_ALL, lineterminator="\n")
header = ["id", "id_siswa", "id_soal", "jawaban"]
writer.writerow(header)

for idx_siswa in range(total_siswa):
    id_siswa = idx_siswa + 1
    for idx_soal in range(total_soal):
        id += 1
        id_soal = idx_soal + 1
        jawaban = fake.random_element(elements=config.pilihan_jawaban)
        writer.writerow([id, id_siswa, id_soal, jawaban])

f.close()
