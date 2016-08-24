from flask_admin.contrib.sqla import ModelView
from app.models import Loja
from wtforms.fields import SelectField
from .formatters import (
    money_formatter, square_meters_formatter, link_formatter, liter_formatter
)


class BaseItemModelView(ModelView):

    can_view_details = True

    column_formatters = dict(
        link_loja=lambda c, v, m, p: link_formatter(
            m.link_loja, 'Ver na loja'),
        capacidade=lambda c, v, m, p: liter_formatter(m.capacidade),
        preco_a_vista=lambda c, v, m, p: money_formatter(m.preco_a_vista),
        preco_parcelado=lambda c, v, m, p: money_formatter(m.preco_parcelado)
    )

    column_exclude_list = (
        'altura', 'largura', 'comprimento'
    )


class ImovelModelView(ModelView):

    can_view_details = True

    column_default_sort = ('nota', True)

    column_exclude_list = (
        'visitado', 'aprovado', 'tem_garagem', 'andar', 'sol', 'nivel_barulho',
        'endereco', 'nota', 'chuveiro', 'tem_portaria', 'tem_elevador',
        'tem_salao_festas', 'parada_onibus', 'linha_onibus',
        'numero_dormitorios', 'mercado', 'shopping', 'farmacia', 'comentarios',
        'posto_gasolina', 'valor_aluguel', 'valor_condominio', 'valor_iptu'
    )

    column_formatters = dict(
        link=lambda c, v, m, p: link_formatter(m.link, 'Ver no site'),
        tamanho=lambda c, v, m, p: square_meters_formatter(m.tamanho),
        valor_total=lambda c, v, m, p: money_formatter(m.valor_total)
    )

    column_filters = ('visitado', 'aprovado', 'valor_total')

    form_args = dict(
        sol=dict(
            choices=[
                ('N/A', 'Não Informado'), ('Norte', 'Norte'),
                ('Sul', 'Sul'), ('Leste', 'Leste'), ('Oeste', 'Oeste')
            ]
        ),
        nota=dict(
            choices=[(x, str(x)) for x in range(0, 6)],
            coerce=int
        ),
        nivel_barulho=dict(
            choices=[(x, str(x)) for x in range(0, 6)],
            coerce=int
        ),
        chuveiro=dict(
            choices=[
                ('N/A', 'Não Informado'), ('Gás', 'Gás'),
                ('Elétrico', 'Elétrico')
            ]
        )
    )

    form_overrides = dict(
        sol=SelectField,
        nota=SelectField,
        nivel_barulho=SelectField,
        chuveiro=SelectField
    )

    def get_column_names(self, only_columns, excluded_columns):

        columns = super().get_column_names(only_columns, excluded_columns)
        columns.insert(1, ('valor_total', 'Valor Total'))

        return columns
