from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

# Format: mysql://[username]:[password]@[host]:[port]/[database]'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://m42nk@localhost/CBT_JATIM'

db = SQLAlchemy(app)

class Mata_Pelajaran(db.Model):
    __tablename__ = "Mata_Pelajaran"

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)

mapel_fields = {
    'id': fields.Integer,
    'nama': fields.String,
}

mapel_post_args = reqparse.RequestParser()
mapel_post_args.add_argument("nama", type=str, required=True)

mapel_put_args = reqparse.RequestParser()
mapel_put_args.add_argument("nama", type=str, required=True)

@api.resource('/mata-pelajaran/', '/mata-pelajaran/<int:mapel_id>')
class Mata_Pelajaran_Resource(Resource):
    @marshal_with(mapel_fields)
    def get(self, mapel_id=None):
        if not mapel_id:
            return Mata_Pelajaran.query.all()

        result = Mata_Pelajaran.query.filter_by(id=mapel_id).first()

        if not result:
            abort(404, message=f"Mapel dengan ID {mapel_id} tidak ditemukan")

        return result


    @marshal_with(mapel_fields)
    def post(self, mapel_id=None):
        if mapel_id:
            abort(400, message="Bad Request")

        args = mapel_post_args.parse_args()

        result = Mata_Pelajaran(nama=args['nama'])

        db.session.add(result)
        db.session.commit()
        return result, 201

    @marshal_with(mapel_fields)
    def put(self, mapel_id=None):
        if not mapel_id:
            abort(400, message=f"ID mapel tidak boleh kosong")

        args = mapel_put_args.parse_args()

        result = Mata_Pelajaran.query.filter_by(id=mapel_id).first()

        if not result:
            abort(404, message=f"Mapel dengan ID {mapel_id} tidak ditemukan")

        if args['nama']:
            result.nama = args['nama']

        db.session.commit()

        return result

    @marshal_with(mapel_fields)
    def delete(self, mapel_id=None):
        if not mapel_id:
            abort(400, message=f"ID mapel tidak boleh kosong")

        deleted = Mata_Pelajaran.query.filter_by(id=mapel_id).delete()

        if not deleted:
            abort(404, message=f"Mapel dengan ID {mapel_id} gagal dihapus, cek apa ID sudah benar")

        db.session.commit()
        return None, 204


if __name__ == "__main__":
    app.run(port=5000, debug=True)
