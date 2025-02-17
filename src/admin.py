import os
from flask_admin import Admin
from models import db, User, Planets, People, Starship, Vehicle, Species, Favoritos
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')
    class FavoritosAdmin(ModelView):
        column_list = ("id", "usuario_id", "planets_id","people_id","starship_id", "vehicle_id", "species_id")
        form_columns = ("usuario_id", "planets_id","people_id","starship_id", "vehicle_id", "species_id")
        column_hide_backrefs = False

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Planets, db.session))
    admin.add_view(ModelView(People, db.session))
    admin.add_view(ModelView(Starship, db.session))
    admin.add_view(ModelView(Vehicle, db.session))
    admin.add_view(ModelView(Species, db.session))
    admin.add_view(FavoritosAdmin(Favoritos, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))