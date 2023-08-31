"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User,Planets, People, Starship, Vehicle, Species, Favoritos
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


## ENDPOINTS USUARIO
@app.route('/user', methods=['GET'])
def handle_hello():

    users_query = User.query.all()

    results= list(map(lambda item: item.serialize(), users_query ))

    if results == []:
        return jsonify({"msg":"no hay usuarios"}), 404

    response_body = {
        "msg": "Hello, estos son los usuarios ",
        "results": results
    }

    return jsonify(response_body), 200


#ENDPOINT PARA USUARIO
@app.route('/user/<int:user_id>', methods=['GET'])
def get_usuario(user_id):

    print(user_id)

    user_query= User.query.filter_by(id = user_id).first()
    

    if user_query is None:
       return jsonify({"msg": "no existe el usuario"}), 404
    

    response_body = {
        "msg": "Hello, este es el usuario ",
        "results" : user_query.serialize()
    }

    return jsonify(response_body), 200

#ENDPOINT PARA PLANETAS
@app.route('/planets', methods=['GET'])
def get_planets():
    
    planets_query = Planets.query.all()
    


    results =list(map(lambda item: item.serialize(), planets_query))
    
    
    if results == []:
        return jsonify({"msg":"no hay planetas"}), 404
    

    response_body = {
        "msg": "Hello, estos son los planetas ",
        "results" : results
    }

    return jsonify(response_body), 200

#ENDPOINT PLANETA
@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):

    print(planet_id)

    planet_query= Planets.query.filter_by(id = planet_id).first()
    

    if planet_query is None:
       return jsonify({"msg": "no existe el planeta"}), 404
    

    response_body = {
        "msg": "Hello, estos son los planetas ",
        "results" : planet_query.serialize()
    }

    return jsonify(response_body), 200

#NEDPOINT PARA PEOPLE
@app.route('/people', methods=['GET'])
def get_peoples():
    
    people_query = People.query.all()
    


    results =list(map(lambda item: item.serialize(), people_query))
    
    
    if results == []:
        return jsonify({"msg":"no hay personas"}), 404
    

    response_body = {
        "msg": "Hello, estas son las personas ",
        "results" : results
    }

    return jsonify(response_body), 200

    #ENDPOINT PARA PERSONA
@app.route('/people/<int:people_id>', methods=['GET'])
def get_people(people_id):

    print(people_id)

    people_query= People.query.filter_by(id = people_id).first()
    

    if people_query is None:
       return jsonify({"msg": "no existe la persona"}), 404
    

    response_body = {
        "msg": "Hello, esta es la persona ",
        "results" : people_query.serialize()
    }

    return jsonify(response_body), 200

#ENDPOINT PARA STARSHIPS
@app.route('/starship', methods=['GET'])
def get_starships():
    
    starships_query = Starship.query.all()
    


    results =list(map(lambda item: item.serialize(), starships_query))
    
    
    if results == []:
        return jsonify({"msg":"no hay starships"}), 404
    

    response_body = {
        "msg": "Hello, estas son las starships ",
        "results" : results
    }

    return jsonify(response_body), 200
#ENDPOINT PARA STARSHIP
@app.route('/starship/<int:starship_id>', methods=['GET'])
def get_starship(starship_id):

    print(starship_id)

    starship_query= Starship.query.filter_by(id = starship_id).first()
    

    if starship_query is None:
       return jsonify({"msg": "no existe el starship"}), 404
    

    response_body = {
        "msg": "Hello, este es el starship ",
        "results" : starship_query.serialize()
    }

    return jsonify(response_body), 200

    #ENDPOINT PARA VEHICLES
@app.route('/vehicle', methods=['GET'])
def get_vehicles():
    
    vehicles_query = Vehicle.query.all()
    


    results =list(map(lambda item: item.serialize(), vehicles_query))
    
    
    if results == []:
        return jsonify({"msg":"no hay vehiculos"}), 404
    

    response_body = {
        "msg": "Hello, estos son los vehiculos ",
        "results" : results
    }

    return jsonify(response_body), 200

#ENDPOINT PARA VEHICULO
@app.route('/vehicle/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):

    print(vehicle_id)

    vehicle_query= Vehicle.query.filter_by(id = vehicle_id).first()
    

    if vehicle_query is None:
       return jsonify({"msg": "no existe el vehicle"}), 404
    

    response_body = {
        "msg": "Hello, este es el vehicle ",
        "results" : vehicle_query.serialize()
    }

    return jsonify(response_body), 200

    #ENDPOINT PARA SPECIES
@app.route('/species', methods=['GET'])
def get_species():
    
    species_query = Species.query.all()
    


    results =list(map(lambda item: item.serialize(), species_query))
    
    
    if results == []:
        return jsonify({"msg":"no hay species"}), 404
    

    response_body = {
        "msg": "Hello, estas son las species ",
        "results" : results
    }

    return jsonify(response_body), 200

#ENDPOINT PARA SPECIE
@app.route('/species/<int:species_id>', methods=['GET'])
def get_specie(species_id):

    print(species_id)

    species_query= Species.query.filter_by(id = species_id).first()
    

    if species_query is None:
       return jsonify({"msg": "no existe la specie"}), 404
    

    response_body = {
        "msg": "Hello, esta es la specie ",
        "results" : species_query.serialize()
    }

    return jsonify(response_body), 200

    #ENPOINT PARA FAVORITOS 
@app.route('/user/favoritos', methods=['GET'])
def get_favoritos():
    
    favoritos_query = Favoritos.query.all()
    


    results =list(map(lambda item: item.serialize(), favoritos_query))
    
    
    if results == []:
        return jsonify({"msg":"no hay favoritos"}), 404
    

    response_body = {
        "msg": "Hello, estos son los favoritos ",
        "results" : results
    }

    return jsonify(response_body), 200

    #ENDPOINT PARA FAVORITO
@app.route('/user/<int:id>/favoritos', methods=['GET'])
def get_favorito(id):


    favoritos_query= Favoritos.query.filter_by(usuario_id = id)
    response = list(map(lambda user : user.serialize(), favoritos_query))

    if response == []:
       return jsonify({"msg": "no existe el favorito"}), 404
    

    response_body = {
        "msg": "Hello, este es el favorito ",
        "results" : response
    }

    return jsonify(response_body), 200

    ## AGREGAR PLANETA A FAVORITO
@app.route('/favoritos/planets/<int:planets1_id>', methods=['POST'])
def create_favorito_planetas(planets1_id):

    request_body = request.json
    #validamos que exista el usuario
    user_query = User.query.filter_by(id = request_body["usuario_id"]).first() #id = propiedad de la tabla user (items de la izq del =)
    if user_query is None:
        return jsonify({"msg": "El usuario no está registrado"}), 404

        #validamos que exista el planeta
    planet_query = Planets.query.filter_by(id = planets1_id).first() #id es la propiedad de la tabla Planets y planeta_id es el valor que se pasa por URL
    if planet_query is None:
        return jsonify({"msg": "El planeta no existe"}), 404

         #validamos que el planeta ya existía como fav
    fav_query = Favoritos.query.filter_by(usuario_id = request_body["usuario_id"]).filter_by(planets_id = planets1_id ).first() #devuelve los valores que coinciden (del user_id la tabla Fav) con el body del postman
    
    if fav_query: #compara el id del planeta del item con el valor pasado por URL
            return jsonify({"msg": "El planeta ya está agregado a favoritos, no se volverá a agregar"}), 404
        
    #Si no se cumplen las condiciones anteriores, se agrega el planeta a favoritos
    new_planet = Favoritos(usuario_id= request_body["usuario_id"], planets_id= planets1_id)
    db.session.add(new_planet)
    db.session.commit()

    request_body={
        "msg": "Planeta agregado a favorito"
    }
    return jsonify(request_body), 200

    ##AGREGAR PEOPLE A FAVORITO
@app.route('/favoritos/people/<int:people1_id>', methods=['POST'])
def create_favorito_people(people1_id):

    request_body = request.json
     #validamos que exista el usuario
    user_query = User.query.filter_by(id = request_body["usuario_id"]).first() #id = propiedad de la tabla user (items de la izq del =)
    if user_query is None:
        return jsonify({"msg": "El usuario no está registrado"}), 404
    
     #validamos que exista el peolpe
    people_query = People.query.filter_by(id = people1_id).first() #id es la propiedad de la tabla Planets y planeta_id es el valor que se pasa por URL
    if people_query is None:
        return jsonify({"msg": "El people no existe"}), 404
    
     #validamos que el people ya existía como fav
    fav_query = Favoritos.query.filter_by(usuario_id = request_body["usuario_id"]).filter_by(people_id = people1_id).first() #devuelve los valores que coinciden (del user_id la tabla Fav) con el body del postman
   
    if fav_query: #compara el id del people del item con el valor pasado por URL
            return jsonify({"msg": "El people ya está agregado a favoritos, no se volverá a agregar"}), 404

    
    new_people = Favoritos(usuario_id= request_body["usuario_id"], people_id= people1_id)
    db.session.add(new_people)
    db.session.commit()

    request_body={
        "msg": "People agregado a favorito"
    }
    return jsonify(request_body), 200

    ## AGREGAR STARSHIP A FAVORITOS
@app.route('/favoritos/starship/<int:starship1_id>', methods=['POST'])
def create_favorito_starship(starship1_id):

    request_body = request.json
   #validamos que exista el usuario
    user_query = User.query.filter_by(id = request_body["usuario_id"]).first() #id = propiedad de la tabla user (items de la izq del =)
    if user_query is None:
        return jsonify({"msg": "El usuario no está registrado"}), 404
    
    #validamos que exista el starship
    starship_query = Starship.query.filter_by(id = starship1_id).first() #id es la propiedad de la tabla Planets y planeta_id es el valor que se pasa por URL
    if starship_query is None:
        return jsonify({"msg": "El starship no existe"}), 404

        #validamos que el starship ya existía como fav
    fav_query = Favoritos.query.filter_by(usuario_id = request_body["usuario_id"]).filter_by(starship_id = starship1_id).first() #devuelve los valores que coinciden (del user_id la tabla Fav) con el body del postman
   
    if fav_query: #compara el id del people del item con el valor pasado por URL
            return jsonify({"msg": "El starship ya está agregado a favoritos, no se volverá a agregar"}), 404


    new_starship = Favoritos(usuario_id= request_body["usuario_id"], starship_id= starship1_id)
    db.session.add(new_starship)
    db.session.commit()

    request_body={
        "msg": "Starship agregado a favorito"
    }
    return jsonify(request_body), 200

    #AGREGAR VEHICLE A FAVORITO
@app.route('/favoritos/vehicle/<int:vehicle1_id>', methods=['POST'])
def create_favorito_vehicle(vehicle1_id):

    request_body = request.json
     #validamos que exista el usuario
    user_query = User.query.filter_by(id = request_body["usuario_id"]).first() #id = propiedad de la tabla user (items de la izq del =)
    if user_query is None:
        return jsonify({"msg": "El usuario no está registrado"}), 404

        #validamos que exista el vehicle
    vehicle_query = Starship.query.filter_by(id = vehicle1_id).first() #id es la propiedad de la tabla Planets y planeta_id es el valor que se pasa por URL
    if vehicle_query is None:
        return jsonify({"msg": "El vehicle no existe"}), 404

         #validamos que el starship ya existía como fav
    fav_query = Favoritos.query.filter_by(usuario_id = request_body["usuario_id"]).filter_by(vehicle_id = vehicle1_id).first() #devuelve los valores que coinciden (del user_id la tabla Fav) con el body del postman
   
    if fav_query: #compara el id del people del item con el valor pasado por URL
            return jsonify({"msg": "El vehicle ya está agregado a favoritos, no se volverá a agregar"}), 404


    new_vehicle = Favoritos(usuario_id= request_body["usuario_id"], vehicle_id= vehicle1_id)
    db.session.add(new_vehicle)
    db.session.commit()

    request_body={
        "msg": "Vehicle agregado a favorito"
    }
    return jsonify(request_body), 200

    ##AGREAGR SPECIE A FAVORITO
@app.route('/favoritos/species/<int:specie1_id>', methods=['POST'])
def create_favorito_specie(specie1_id):

    request_body = request.json
    #validamos que exista el usuario
    user_query = User.query.filter_by(id = request_body["usuario_id"]).first() #id = propiedad de la tabla user (items de la izq del =)
    if user_query is None:
        return jsonify({"msg": "El usuario no está registrado"}), 404
    
    #validamos que exista el specie
    specie_query = Species.query.filter_by(id = specie1_id).first() #id es la propiedad de la tabla Planets y planeta_id es el valor que se pasa por URL
    if specie_query is None:
        return jsonify({"msg": "El specie no existe"}), 404
    
    #validamos que el specie ya existía como fav
    fav_query = Favoritos.query.filter_by(usuario_id = request_body["usuario_id"]).filter_by(species_id = specie1_id).first() #devuelve los valores que coinciden (del user_id la tabla Fav) con el body del postman
   
    if fav_query: #compara el id del people del item con el valor pasado por URL
            return jsonify({"msg": "El specie ya está agregado a favoritos, no se volverá a agregar"}), 404

    
    new_specie = Favoritos(usuario_id= request_body["usuario_id"], species_id= specie1_id)
    db.session.add(new_specie)
    db.session.commit()

    request_body={
        "msg": "Specie agregado a favorito"
    }
    return jsonify(request_body), 200


    ##BORRAR PLANETAS DE FAVORITO
@app.route('/favoritos/planets/<int:planets1_id>', methods=['DELETE'])
def borrar_favorito_planetas(planets1_id):

    request_body = request.json
    #validamos que exista el usuario
    user_query = User.query.filter_by(id = request_body["usuario_id"]).first() #id = propiedad de la tabla user (items de la izq del =)
    if user_query is None:
        return jsonify({"msg": "El usuario no está registrado"}), 404

        #validamos que exista el planeta
    planet_query = Planets.query.filter_by(id = planets1_id).first() #id es la propiedad de la tabla Planets y planeta_id es el valor que se pasa por URL
    if planet_query is None:
        return jsonify({"msg": "El planeta no existe"}), 404

         #validamos que el planeta ya existía como fav
    fav_query = Favoritos.query.filter_by(usuario_id = request_body["usuario_id"]).filter_by(planets_id = planets1_id ).first() #devuelve los valores que coinciden (del user_id la tabla Fav) con el body del postman
    
        
    #Si no se cumplen las condiciones anteriores, se elimina el planeta a favoritos
    
    db.session.delete(fav_query)
    db.session.commit()

    request_body={
        "msg": "Planeta eliminado de favorito"
    }
    return jsonify(request_body), 200


##BORRAR PEOPLE DE FAVORITO
@app.route('/favoritos/people/<int:people1_id>', methods=['DELETE'])
def eliminar_favorito_people(people1_id):

    request_body = request.json
     #validamos que exista el usuario
    user_query = User.query.filter_by(id = request_body["usuario_id"]).first() #id = propiedad de la tabla user (items de la izq del =)
    if user_query is None:
        return jsonify({"msg": "El usuario no está registrado"}), 404
    
     #validamos que exista el peolpe
    people_query = People.query.filter_by(id = people1_id).first() #id es la propiedad de la tabla Planets y planeta_id es el valor que se pasa por URL
    if people_query is None:
        return jsonify({"msg": "El people no existe"}), 404
    
     #validamos que el people ya existía como fav
    fav_query = Favoritos.query.filter_by(usuario_id = request_body["usuario_id"]).filter_by(people_id = people1_id).first() #devuelve los valores que coinciden (del user_id la tabla Fav) con el body del postman
    
    db.session.delete(fav_query)
    db.session.commit()

    request_body={
        "msg": "People eliminado de favorito"
    }
    return jsonify(request_body), 200

##BORRAR STARSHIP DE FAVORITOS
@app.route('/favoritos/starship/<int:starship1_id>', methods=['DELETE'])
def eliminar_favorito_starship(starship1_id):

    request_body = request.json
   #validamos que exista el usuario
    user_query = User.query.filter_by(id = request_body["usuario_id"]).first() #id = propiedad de la tabla user (items de la izq del =)
    if user_query is None:
        return jsonify({"msg": "El usuario no está registrado"}), 404
    
    #validamos que exista el starship
    starship_query = Starship.query.filter_by(id = starship1_id).first() #id es la propiedad de la tabla Planets y planeta_id es el valor que se pasa por URL
    if starship_query is None:
        return jsonify({"msg": "El starship no existe"}), 404

        #validamos que el starship ya existía como fav
    fav_query = Favoritos.query.filter_by(usuario_id = request_body["usuario_id"]).filter_by(starship_id = starship1_id).first() #devuelve los valores que coinciden (del user_id la tabla Fav) con el body del postman
    
    db.session.delete(fav_query)
    db.session.commit()

    request_body={
        "msg": "Starship eliminado de favorito"
    }
    return jsonify(request_body), 200

    ##BORRAR VEHICLE DE FAVORITO
@app.route('/favoritos/vehicle/<int:vehicle1_id>', methods=['DELETE'])
def eliminar_favorito_vehicle(vehicle1_id):

    request_body = request.json
     #validamos que exista el usuario
    user_query = User.query.filter_by(id = request_body["usuario_id"]).first() #id = propiedad de la tabla user (items de la izq del =)
    if user_query is None:
        return jsonify({"msg": "El usuario no está registrado"}), 404

        #validamos que exista el vehicle
    vehicle_query = Starship.query.filter_by(id = vehicle1_id).first() #id es la propiedad de la tabla Planets y planeta_id es el valor que se pasa por URL
    if vehicle_query is None:
        return jsonify({"msg": "El vehicle no existe"}), 404

         #validamos que el starship ya existía como fav
    fav_query = Favoritos.query.filter_by(usuario_id = request_body["usuario_id"]).filter_by(vehicle_id = vehicle1_id).first() #devuelve los valores que coinciden (del user_id la tabla Fav) con el body del postman
    
    db.session.delete(fav_query)
    db.session.commit()

    request_body={
        "msg": "Vehicle eliminado de favorito"
    }
    return jsonify(request_body), 200


    ##BORRAR SPECIE DE FAVORITO
@app.route('/favoritos/species/<int:specie1_id>', methods=['DELETE'])
def eliminar_favorito_specie(specie1_id):

    request_body = request.json
    #validamos que exista el usuario
    user_query = User.query.filter_by(id = request_body["usuario_id"]).first() #id = propiedad de la tabla user (items de la izq del =)
    if user_query is None:
        return jsonify({"msg": "El usuario no está registrado"}), 404
    
    #validamos que exista el specie
    specie_query = Species.query.filter_by(id = specie1_id).first() #id es la propiedad de la tabla Planets y planeta_id es el valor que se pasa por URL
    if specie_query is None:
        return jsonify({"msg": "El specie no existe"}), 404
    
    #validamos que el specie ya existía como fav
    fav_query = Favoritos.query.filter_by(usuario_id = request_body["usuario_id"]).filter_by(species_id = specie1_id).first() #devuelve los valores que coinciden (del user_id la tabla Fav) con el body del postman
   
    db.session.delete(fav_query)
    db.session.commit()

    request_body={
        "msg": "Specie eliminado de favorito"
    }
    return jsonify(request_body), 200
###ENDPOINT PARA SING UP

@app.route("/sing_up", methods=["POST"])
def sing_up():
    request_body = request.json


    usuario= User(email=request_body["email"], password=request_body["password"], name=request_body["name"], apellido=request_body["apellido"])
    db.session.add(usuario)
    db.session.commit()
    
    return {
        "results": usuario.serialize()
    }
    

    ##ENDPOINT LOGIN
@app.route("/login", methods=["POST"])
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    user_query= User.query.filter_by(email=email).first()

    if user_query is None:
         return jsonify({"msg": "Email dosn't exist"}), 404



    if email != user_query.email or password != user_query.password:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=email)

    response_body = {
        "access_token": access_token,
        "email": user_query.serialize()
    }
    return jsonify(response_body)

    ##PROTEGER LA RUTA
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


if __name__ == "__main__":
    app.run()

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
