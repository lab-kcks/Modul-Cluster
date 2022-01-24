import csv
import config

f = open('csv/mata_pelajaran.csv', 'w')
writer = csv.writer(f)

header = ['id', 'nama']
writer.writerow(header)

id = 1
for _mapel in config.mata_pelajaran:
    id = id + 1
    writer.writerow([id,_mapel])

f.close()

