from . import db, Base


categories = [
    'Eletrodomestico', 'Móvel', 'Cozinha', 'Banheiro', 'Eletrônico',
    'Decoração', 'Quarto', 'Sala'
]

priorities = [
    (0, 'Nenhuma'), (1, 'Baixa'), (2, 'Média'), (3, 'Moderada'), (4, 'Alta'),
    (5, 'Altíssima'), (6, 'Urgente'), (7, 'Imprescindível')
]


class CheckListItem(Base):

    __tablename__ = 'checklist_items'

    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String())
    categoria = db.Column(db.String())
    prioridade = db.Column(db.Integer())
    finalizado = db.Column(db.Boolean())
