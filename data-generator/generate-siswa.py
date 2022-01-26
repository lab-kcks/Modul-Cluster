from faker import Faker
import csv
import config

# inisiasi objek Faker
fake = Faker()

# Format nrp (14 digit): <3-digit-id-kota><x-digit-padding><urutan-siswa-di-kota>
# contoh: 02100000000123
# 021 - id kota
# 000123 - urutan siswa di kota

# Jumlah 38 kota
# 001 - 038

total_kota = len(config.kota)
total_siswa = config.total_siswa
id = 0

f = open("csv/siswa.csv", "w")
writer = csv.writer(f, doublequote=True, quoting=csv.QUOTE_ALL, lineterminator="\n")
header = ["id", "id_kota", "nrp", "nama"]

writer.writerow(header)

for idx_kota in range(total_kota):
    id_kota = idx_kota + 1

    # zfill = menambahkan 0 di depan sampai panjang n (padding)
    prefix_kota = str(id_kota).zfill(3)
    for idx_siswa in range(total_siswa):
        id += 1
        nrp = prefix_kota + str(idx_siswa + 1).zfill(config.panjang_nrp - 3)
        nama = fake.name()
        row = [id, id_kota, nrp, nama]
        writer.writerow(row)

f.close()
