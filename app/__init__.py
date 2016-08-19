from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .models import db, Loja
from .models.auth import User, Role
from .models.eletrodomesticos import Geladeira, Fogao, Microondas
from .blueprints.error_handler import error_handler


def factory(config):
    """
    Flask Application Factory function

    Generate a new Flask application through this function by specifying
    a config object.

    Args:
        config: The configuration class to be used.
    """

    app = Flask(__name__)

    config = config or 'DefaultConfig'
    app.config.from_object('etc.config.{}'.format(config))

    auth_datastore = SQLAlchemyUserDatastore(db, User, Role)
    Security(app, auth_datastore)
    db.init_app(app)

    if app.config['RECREATE_DATABASE']:
        with app.app_context():
            db.drop_all()
            db.create_all()

    app.register_blueprint(error_handler)

    admin = Admin(
        app,
        'Casa Planner',
        template_mode='bootstrap3',
        url='/'
    )

    with app.app_context():

        admin.add_view(
            ModelView(
                Geladeira,
                db.session,
                category='Eletrodomesticos',
                name='Geladeiras',
                endpoint='geladeiras'
            )
        )

        admin.add_view(
            ModelView(
                Fogao,
                db.session,
                category='Eletrodomesticos',
                name='Fogões',
                endpoint='fogoes'
            )
        )

        admin.add_view(
            ModelView(
                Microondas,
                db.session,
                category='Eletrodomesticos',
                name='Microondas',
                endpoint='microondas'
            )
        )

        admin.add_view(
            ModelView(
                Loja,
                db.session,
                name='Lojas',
                endpoint='lojas'
            )
        )

    return app
