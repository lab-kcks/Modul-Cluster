# Data Generator

Note:
1. buat database
`mysql -e "drop database if exists CBT_JATIM; create database CBT_JATIM;"`

2. generate schema (tabel)
`python generate-schema.py`

3. generate data (isi tabel)
`python generate-all.py`

5. import data csv ke database:
`mysql < import-from-csv.sql`
