from flask_admin.contrib.sqla import ModelView
from flask import Markup
from app.models import Loja


class BaseItemModelView(ModelView):

    can_view_details = True

    column_formatters = dict(
        link_loja=lambda c, v, m, p: Markup(
            "<a href='{}'> Ver na Loja </a>".format(m.link_loja)
        ),
        capacidade=lambda c, v, m, p: '{} L'.format(m.capacidade)
    )

    column_exclude_list = ('altura', 'largura', 'comprimento')


class ImovelModelView(ModelView):

    can_view_details = True

    column_exclude_list = ('visitado', 'aprovado', 'tem_garagem')

    column_formatters = dict(
        link=lambda c, v, m, p: Markup(
            "<a href='{}'> Ver no site </a>".format(m.link)
        ),
        tamanho=lambda c, v, m, p: '{} m'.format(m.tamanho)
    )
