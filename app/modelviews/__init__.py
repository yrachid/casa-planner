from flask_admin.contrib.sqla import ModelView
from .formatters import (
    money_formatter, link_formatter, liter_formatter, centimeters_formatter
)


class BaseItemModelView(ModelView):

    can_view_details = True

    column_formatters = dict(
        link_loja=lambda c, v, m, p: link_formatter(
            m.link_loja, 'Ver na loja'),
        capacidade=lambda c, v, m, p: liter_formatter(m.capacidade),
        preco_a_vista=lambda c, v, m, p: money_formatter(m.preco_a_vista),
        preco_parcelado=lambda c, v, m, p: money_formatter(m.preco_parcelado),
        altura=lambda c, v, m, p: centimeters_formatter(m.altura),
        largura=lambda c, v, m, p: centimeters_formatter(m.largura),
        comprimento=lambda c, v, m, p: centimeters_formatter(m.comprimento)
    )

    column_exclude_list = (
        'altura', 'largura', 'comprimento'
    )
