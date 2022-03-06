from faker import Faker
import csv
import config
import json

fake = Faker()

total_siswa = config.total_siswa * len(config.kota)
total_soal = config.total_soal
id = 0

file_number = 1

def create_file():
    global file_number

    # f = open("csv/jawaban.csv", "w")
    f = open(f"csv/jawaban-{file_number}.csv", "w")
    writer = csv.writer(f, doublequote=True, quoting=csv.QUOTE_ALL, lineterminator="\n")
    header = ["id", "id_siswa", "id_soal", "id_mapel", "jawaban"]
    writer.writerow(header)
    return [writer, f]

[writer, f] = create_file()

for idx_siswa in range(total_siswa):
    id_siswa = idx_siswa + 1

    print("id_siswa: ", id_siswa, "|", "file_number: ", file_number)

    if id_siswa % config.total_siswa == 0 or id_siswa >= total_siswa - config.total_siswa:
        f.close()
        [writer, f] = create_file()
        file_number += 1

    for idx_mapel in range(len(config.mata_pelajaran)) :
        id_mapel = idx_mapel+1
        for idx_soal in range(total_soal):
            id += 1
            id_soal = idx_soal + 1
            jawaban = fake.random_element(elements=config.pilihan_jawaban)
            writer.writerow([id, id_siswa, id_soal, id_mapel, jawaban])
