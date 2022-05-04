from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship


db = SQLAlchemy()

class Estado(db.Model):
    __tablename__ = 'estado'

    id_estado = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False) 
    siglasrenapo = db.Column(db.String(255), nullable=False) 
    numero_oficial = db.Column(db.Integer)


class Municipio(db.Model):
    __tablename__ = 'municipio'

    id_municipio = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False) 
    estado_id = db.Column(db.Integer, db.ForeignKey('estado.id_estado'))
    estado = db.relationship(Estado) 


class CodigoPostal(db.Model):
    __tablename__ = 'codigo_postal'

    id_codigo_postal = db.Column(db.Integer, primary_key=True)
    colonia = db.Column(db.String(255), nullable=False)
    ciudad = db.Column(db.String(255), nullable=False)
    municipio_id = db.Column(db.Integer, db.ForeignKey('municipio.id_municipio'))
    municipio = db.relationship(Municipio)
    asentamiento =  db.Column(db.String(255), nullable=False)
    codigo_postal = db.Column(db.String(5), nullable=False)

