from faker import Faker
import csv
import config
import json

fake = Faker()

total_siswa = config.total_siswa * len(config.kota) + (config.total_siswa * 9)
total_soal = config.total_soal
id = 0

file_number = 1

print("total siswa: ", total_siswa)

def create_file():
    global file_number

    # f = open("csv/jawaban.csv", "w")
    f = open(f"csv/jawaban-{file_number}.csv", "w")
    print("file_number: ", file_number)
    writer = csv.writer(f, doublequote=True, quoting=csv.QUOTE_ALL, lineterminator="\n")
    header = ["id", "id_siswa", "id_soal", "id_mapel", "jawaban"]
    writer.writerow(header)
    return [writer, f]

[writer, f] = create_file()

for idx_siswa in range(total_siswa):
    id_siswa = idx_siswa + 1

    for idx_mapel in range(len(config.mata_pelajaran)) :
        id_mapel = idx_mapel+1
        for idx_soal in range(total_soal):
            id += 1
            id_soal = idx_soal + 1
            jawaban = fake.random_element(elements=config.pilihan_jawaban)
            writer.writerow([id, id_siswa, id_soal, id_mapel, jawaban])
        
    if id_siswa % 12500 == 0:
        print("id siswa processed: ", id_siswa)
        f.close()
        file_number += 1
        [writer, f] = create_file()