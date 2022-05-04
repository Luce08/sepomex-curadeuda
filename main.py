from flask import Flask
from flask import jsonify
from config import config
from models import db
from models import *
from flask import request
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object(enviroment)
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app

enviroment = config['development']
app = create_app(enviroment)
jwt = JWTManager(app)
    
@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if username != 'prueba' or password != 'prueba':
            return jsonify({'data': 'Credenciales Incorrectas'}), 401

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    except Exception as e:
        print(e)

@app.route('/colonias/<codigo_postal>/', methods=['GET'])
@jwt_required()
def obtener_colonias(codigo_postal):
    try:
        rest_colonias = CodigoPostal.query.filter(codigo_postal=codigo_postal).all
        if not rest_colonias:
            error="sin resultados"
            return jsonify(error),204
        results_colonias = {
            "results_colonias": [{"colonia": result_colonia.colonia, "cp":result_colonia.codigo_postal,"ciudad":result_colonia.ciudad,"municipio":result_colonia.municipio} for result_colonia in rest_colonias.items]
            
        }
        return jsonify(results_colonias)
    except Exception as e:
        print(e)


@app.route('/colonias_nombres/<nombre>', methods=['GET'])
@jwt_required()
def obtener_colonias_nombres(nombre):
    try:
        rest_colonias = CodigoPostal.query.filter(colonia=nombre).all
        if not rest_colonias:
            error="sin resultados"
            return jsonify(error),204
        results_colonias = {
            "results_colonias": [{"colonia": result_colonia.colonia, "cp":result_colonia.codigo_postal,"ciudad":result_colonia.ciudad,"municipio":result_colonia.municipio} for result_colonia in rest_colonias.items]
            
        }
        return jsonify(results_colonias)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run(debug=True)
