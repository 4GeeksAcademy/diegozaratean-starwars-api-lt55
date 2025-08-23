import os
from flask_admin import Admin
from models import db, User, Empresa, Videojuego
from flask_admin.contrib.sqla import ModelView

class VideojuegoAdmin(ModelView):
    column_list = ('id', 'nombre', 'year', 'empresa')
    form_columns = ('nombre', 'year', 'empresa')

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'darkly'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))

    admin.add_view(ModelView(Empresa, db.session))

    # admin.add_view(ModelView(Videojuego, db.session))
    admin.add_view(VideojuegoAdmin(Videojuego, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))