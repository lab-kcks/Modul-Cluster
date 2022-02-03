"""
Opsi lain untuk bikin schema sql
"""

from sqlalchemy import *

db_username = 'm42nk'
db_host = 'localhost'
db_name = 'CBT_JATIM'

engine = create_engine(f'mysql://{db_username}@{db_host}/{db_name}')
metadata_obj = MetaData(engine)

metadata_obj.drop_all()

Table('Kota', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('nama', String(255)),
)

Table('Mata_Pelajaran', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('nama', String(255)),
)

Table('Siswa', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('id_kota', Integer, ForeignKey("Kota.id"), nullable=false),
    Column('nrp', String(255)),
    Column('nama', String(255)),
)

Table('Soal', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('id_mapel', Integer, ForeignKey("Mata_Pelajaran.id"), nullable=false),
    Column('body', String(255)),
    Column('pilihan_jawaban', String(255)),
    Column('jawaban_benar', String(1)),
)

Table('Jawaban', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('id_siswa', Integer, ForeignKey("Siswa.id"), nullable=false),
    Column('id_soal', Integer, ForeignKey("Soal.id"), nullable=false),
    Column('id_mapel', Integer, ForeignKey("Mata_Pelajaran.id"), nullable=false),
    Column('jawaban', String(1)),
)

"""
Table('Result', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('id_siswa', Integer, ForeignKey("Siswa.id"), nullable=false),
    Column('id_soal', Integer, ForeignKey("Soal.id"), nullable=false),
    Column('id_mapel', Integer, ForeignKey("Mata_Pelajaran.id"), nullable=false),
    Column('is_jawaban_benar', Boolean),
)
"""

metadata_obj.create_all()

