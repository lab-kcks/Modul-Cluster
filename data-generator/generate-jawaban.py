from faker import Faker
import csv
import config
import json

fake = Faker()

total_siswa = config.total_siswa
total_soal = config.total_soal
total_kota = len(config.kota)
id = 0

f = open("csv/jawaban.csv", "w")
writer = csv.writer(f, doublequote=True, quoting=csv.QUOTE_ALL, lineterminator="\n")
header = ["id", "id_siswa", "id_soal", "id_mapel", "jawaban"]
writer.writerow(header)

# bikin biar berhubungan sama id kota, kalo id kota 30-38 ntar total siswa dikali 2
for idx_kota in range(total_kota):
    id_kota = idx_kota + 1
    print("processing id_kota : %d" % id_kota)
    if id_kota in range(30, 38 + 1):
        total_siswa = total_siswa * 2

    flag = 0

    for idx_siswa in range(total_siswa):
        id_siswa = idx_siswa + 1
        for idx_mapel in range(len(config.mata_pelajaran)) :
            # print(mapel)
            id_mapel = idx_mapel+1
            for idx_soal in range(total_soal):
                id += 1
                id_soal = idx_soal + 1
                jawaban = fake.random_element(elements=config.pilihan_jawaban)
                writer.writerow([id, id_siswa, id_soal, id_mapel, jawaban])
                flag += 1
    print("%d jawaban generated" % flag)
    
    print("jawaban siswa id_kota %d generated" % id_kota)
    total_siswa = config.total_siswa

f.close()
