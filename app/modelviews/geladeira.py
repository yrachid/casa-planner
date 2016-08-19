from flask_admin.contrib.sqla import ModelView
from app.models import Loja


class GeladeiraModelView(ModelView):
    inline_models = (Loja,)
