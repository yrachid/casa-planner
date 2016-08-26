from flask import Flask
from flask_security import Security, SQLAlchemyUserDatastore
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .models import db, Loja
from .models.auth import User, Role
from .models.moveis import BalcaoCooktop, Sofa, GuardaRoupa
from .models.eletrodomesticos import Geladeira, Fogao, Microondas
from .models.imoveis import Imovel, Bairro, Imobiliaria
from .models.checklist import CheckListItem
from .models.mercado import ItemDespensa, GrupoDespensa
from .modelviews import BaseItemModelView
from .modelviews.imovel import ImovelModelView
from .modelviews.checklist import ChecklistModelView
from .modelviews.mercado import ItemDespensaModelView
from .blueprints.error_handler import error_handler
from .blueprints.restful import mobile_api


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
    app.register_blueprint(mobile_api)

    admin = Admin(
        app,
        'Casa Planner',
        template_mode='bootstrap3',
        url='/',
        index_view=ChecklistModelView(
            CheckListItem,
            db.session,
            name='Checklist',
            url='/',
            endpoint='admin'
        )
    )

    with app.app_context():

        admin.add_view(
            BaseItemModelView(
                Geladeira,
                db.session,
                category='Eletrodomesticos',
                name='Geladeiras',
                endpoint='geladeiras'
            )
        )

        admin.add_view(
            BaseItemModelView(
                Fogao,
                db.session,
                category='Eletrodomesticos',
                name='Fogões',
                endpoint='fogoes'
            )
        )

        admin.add_view(
            BaseItemModelView(
                Microondas,
                db.session,
                category='Eletrodomesticos',
                name='Microondas',
                endpoint='microondas'
            )
        )

        admin.add_view(
            BaseItemModelView(
                BalcaoCooktop,
                db.session,
                category='Moveis',
                name='Balcão Cooktop',
                endpoint='balcoes-cooktop'
            )
        )

        admin.add_view(
            BaseItemModelView(
                GuardaRoupa,
                db.session,
                category='Moveis',
                name='Guarda roupa',
                endpoint='guardas-roupas'
            )
        )

        admin.add_view(
            BaseItemModelView(
                Sofa,
                db.session,
                category='Moveis',
                name='Sofás',
                endpoint='sofas'
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

        admin.add_view(
            ModelView(
                Bairro,
                db.session,
                category='Imoveis',
                name='Bairros',
                endpoint='bairros'
            )
        )

        admin.add_view(
            ModelView(
                Imobiliaria,
                db.session,
                category='Imoveis',
                name='Imobiliarias',
                endpoint='imobiliarias'
            )
        )

        admin.add_view(
            ImovelModelView(
                Imovel,
                db.session,
                category='Imoveis',
                name='Aluguel',
                endpoint='alugueis'
            )
        )

        admin.add_view(
            ItemDespensaModelView(
                ItemDespensa,
                db.session,
                category='Despensa',
                name='Itens',
                endpoint='itens-despensa'
            )
        )

        admin.add_view(
            ModelView(
                GrupoDespensa,
                db.session,
                category='Despensa',
                name='Grupos Despensa',
                endpoint='grupos-despensa'
            )
        )

    return app
