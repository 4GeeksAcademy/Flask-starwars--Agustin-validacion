from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=True)
    apellido = db.Column(db.String(120), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(80), unique=False, nullable=True)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "apellido": self.apellido,
            "email": self.email,
            "password": self.password,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }
    
class Planets(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    rotation_period =  db.Column(db.String(250), nullable=False)
    orbital_period = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    superface_water = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "superface_water": self.superface_water,
            "population": self.climate,

            # do not serialize the password, its a security breach
        }

class People(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String(250), nullable=False)
    mass = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<People %r>' % self.id
    
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,

            # do not serialize the password, its a security breach
        }

class Starship(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)
    cost_in_credits = db.Column(db.String(250), nullable=False)
    length = db.Column(db.String(250), nullable=False)
    max_atmosphering_speed = db.Column(db.String(250), nullable=False)
    crew = db.Column(db.String(250), nullable=False)
    passagers = db.Column(db.String(250), nullable=False)
    cargo_capacity = db.Column(db.String(250), nullable=False)
    consumable = db.Column(db.String(250), nullable=False)
    pilots = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Starship %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "crew": self.crew,
            "passagers": self.passagers,
            "cargo_capacity": self.cargo_capacity,
            "consumable": self.consumable,
            "pilots": self.pilots,


            # do not serialize the password, its a security breach
        }


class Vehicle(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    manufacturer = db.Column(db.String(250), nullable=False)
    cost_in_credits = db.Column(db.String(250), nullable=False)
    length = db.Column(db.String(250), nullable=False)
    max_atmosphering_speed = db.Column(db.String(250), nullable=False)
    crew = db.Column(db.String(250), nullable=False)
    passagers = db.Column(db.String(250), nullable=False)
    cargo_capacity = db.Column(db.String(250), nullable=False)
    consumable = db.Column(db.String(250), nullable=False)
    vehicle_class  = db.Column(db.String(250), nullable=False)
    pilots = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Vehicle %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "crew": self.crew,
            "passagers": self.passagers,
            "cargo_capacity": self.cargo_capacity,
            "consumable": self.consumable,
            "vehicle_class": self.vehicle_class,
            "pilots": self.pilots,


            # do not serialize the password, its a security breach
        }

class Species(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    classification = db.Column(db.String(250), nullable=False)
    designation = db.Column(db.String(250), nullable=False)
    average_height = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    language = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Species %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "classification": self.classification,
            "designation": self.designation,
            "average_height": self.average_height,
            "skin_color": self.skin_color,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "language": self.language,
        

            # do not serialize the password, its a security breach
        }
    

class Favoritos(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))
    starship_id = db.Column(db.Integer, db.ForeignKey('starship.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'))
    usuario = db.relationship(User)
    planets = db.relationship(Planets)
    people = db.relationship(People)
    starship = db.relationship(Starship)
    vehicle = db.relationship(Vehicle)
    species = db.relationship(Species)

    def __repr__(self):
        return '<Favoritos %r>' % self.id

    def serialize(self):
        planetaInfo= Planets.query.filter_by(id=self.planets_id).first()
        peopleInfo= People.query.filter_by(id=self.people_id).first()
        starshipInfo= Starship.query.filter_by(id=self.starship_id).first()
        vehicleInfo= Vehicle.query.filter_by(id=self.vehicle_id).first()
        speciesInfo= Species.query.filter_by(id=self.species_id).first()

        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "planet": None if planetaInfo is None else planetaInfo.serialize() ,
            "people": None if peopleInfo is None else peopleInfo.serialize(),
            "starship": None if starshipInfo is None else starshipInfo.serialize(),
            "vehicle": None if vehicleInfo is None else vehicleInfo.serialize(),
            "species": None if speciesInfo is None else speciesInfo.serialize(),
            # do not serialize the password, its a security breach
        }