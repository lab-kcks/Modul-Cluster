import csv
import config

f = open('csv/kota.csv', 'w')
writer = csv.writer(f)

header = ['id', 'nama']
writer.writerow(header)

id = 1
for _kota in config.kota:
    id = id + 1
    writer.writerow([id,_kota])

f.close()
