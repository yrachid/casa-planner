from flask import Blueprint, jsonify, current_app
from sqlalchemy.ext.declarative import DeclarativeMeta
from app.models import db
from app.models.imoveis import Imovel
import json
mobile_api = Blueprint('api', __name__, url_prefix='/api')


def new_alchemy_encoder():
    _visited_objs = []

    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if not isinstance(obj.__class__, DeclarativeMeta):
                return json.JSONEncoder.default(self, obj)

            if obj in _visited_objs:
                return None
            _visited_objs.append(obj)

            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata' and '_id' not in x]:
                fields[field] = obj.__getattribute__(field)

            return fields

    return AlchemyEncoder


@mobile_api.route('/')
def index():
    return jsonify([])


@mobile_api.route('/alugueis')
def alugueis():

    with current_app.app_context():

        imoveis = json.dumps(
            db.session.query(Imovel).all(),
            cls=new_alchemy_encoder(),
            check_circular=False
        )
        return imoveis
