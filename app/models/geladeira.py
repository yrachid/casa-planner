from . import db, BaseItem


class Geladeira(db.Model, BaseItem):

    __tablename__ = 'geladeiras'

    id = db.Column(db.Integer(), primary_key=True)

    modelo = db.Column(db.String())
    capacidade = db.Column(db.Integer())
