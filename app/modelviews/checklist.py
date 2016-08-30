from flask_admin.contrib.sqla import ModelView
from wtforms.fields import SelectField
from flask_admin.contrib.sqla.filters import FilterEqual
from ..models.checklist import categories, priorities, CheckListItem


class ChecklistModelView(ModelView):

    column_filters = (
        'nome',
        'finalizado',
        FilterEqual(
            column=CheckListItem.categoria,
            name='Categoria',
            options=[
                (c, c) for c in categories
            ]
        )
    )

    page_size = 50

    form_args = dict(
        categoria=dict(
            choices=[(item, item) for item in categories]
        ),
        prioridade=dict(
            choices=priorities,
            coerce=int
        )
    )

    form_overrides = dict(
        categoria=SelectField,
        prioridade=SelectField,
    )
