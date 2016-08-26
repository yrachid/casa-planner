from flask_admin.contrib.sqla import ModelView
from .formatters import stock_unit


class ItemDespensaModelView(ModelView):

    column_exclude_list = ('unidade', )

    column_formatters = dict(
        estoque_minimo=lambda c, v, m, p: stock_unit(
            m.estoque_minimo, m.unidade
        ),
        estoque=lambda c, v, m, p: stock_unit(
            m.estoque, m.unidade
        ),
        marca=lambda c, v, m, p: m.marca or '-'
    )
