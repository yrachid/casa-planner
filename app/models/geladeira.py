from . import db, BaseItem, Base


class Geladeira(Base, BaseItem):

    __tablename__ = 'geladeiras'

    id = db.Column(db.Integer(), primary_key=True)

    modelo = db.Column(db.String())
    outro_modelo = db.Column(db.String())
    capacidade = db.Column(db.Integer())
