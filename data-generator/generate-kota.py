import csv
import config

# buka file yang akan ditulis dengan mode write (akan melakukan overwrite)
f = open('csv/kota.csv', 'w')

# inisiasi `writer` dari csv untuk dapat menulis kedalam file csv
writer = csv.writer(f, doublequote=True, quoting=csv.QUOTE_ALL, lineterminator="\n")

# header yang akan ditulis (berupa list)
header = ['id', 'nama']

# tulis header ke file csv
writer.writerow(header)

id = 0

# looping untuk menulis data ke file csv
for _kota in config.kota:
    id += 1

    # tulis baris ke file csv
    writer.writerow([id,_kota])

# tutup file agar tidak terjadi error
f.close()
