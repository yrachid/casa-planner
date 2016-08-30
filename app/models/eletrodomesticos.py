from . import db, BaseItem, Base


class Geladeira(Base, BaseItem):

    __tablename__ = 'geladeiras'

    id = db.Column(db.Integer(), primary_key=True)

    capacidade = db.Column(db.Integer())


class Fogao(Base, BaseItem):

    __tablename__ = 'fogoes'

    id = db.Column(db.Integer(), primary_key=True)
    numero_bocas = db.Column(db.Integer())


class Microondas(Base, BaseItem):

    __tablename__ = 'microondas'

    id = db.Column(db.Integer(), primary_key=True)
    capacidade = db.Column(db.Integer())


class MaquinaDeLavar(Base, BaseItem):

    __tablename__ = 'maquinas_de_lavar'

    id = db.Column(db.Integer(), primary_key=True)
    capacidade = db.Column(db.Float())
