from flask_admin.contrib.sqla import ModelView
from wtforms.fields import SelectField
from ..models.checklist import categories, priorities


class ChecklistModelView(ModelView):

    column_filters = ('finalizado', )

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
