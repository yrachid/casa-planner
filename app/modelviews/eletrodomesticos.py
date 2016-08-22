from flask_admin.contrib.sqla import ModelView
from flask import Markup
from app.models import Loja


class BaseItemModelView(ModelView):
    column_formatters = dict(
        link_loja=lambda c, v, m, p: Markup(
            "<a href='{}'> Ver na Loja </a>".format(m.link_loja)
        )
    )


class GeladeiraModelView(ModelView):
    pass


class FogaoModelView(ModelView):
    pass
