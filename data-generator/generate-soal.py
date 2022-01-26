from faker import Faker
import csv
import config
import json

# inisiasi object Faker
fake = Faker()

# ambil total soal dari config
total_soal = config.total_soal
id = 0

f = open("csv/soal.csv", "w")
writer = csv.writer(f, doublequote=True, quoting=csv.QUOTE_ALL, lineterminator="\n")
header = ["id", "id_mapel", "body", "pilihan_jawaban", "jawaban_benar"]
writer.writerow(header)

total_mapel = len(config.mata_pelajaran)
for idx_mapel in range(total_mapel):
    id_mapel = idx_mapel + 1
    for i in range(total_soal):
        id += 1

        # gunakan faker untuk membuat susunan string random maksimal 200 karakter
        body = fake.paragraph(nb_sentences=2)

        pilihan_jawaban = dict()
        for pilihan in config.pilihan_jawaban:
            pilihan_jawaban[pilihan] = fake.paragraph(nb_sentences=1)

        # pilih satu jawaban random berdasarkan list dari config
        jawaban_benar = fake.random_element(elements=config.pilihan_jawaban)

        writer.writerow([id, id_mapel, body, pilihan_jawaban, jawaban_benar])

f.close()
