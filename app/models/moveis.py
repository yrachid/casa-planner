from . import db, Base, BaseItem


class BalcaoCooktop(Base, BaseItem):

    __tablename__ = 'balcoes_cooktop'

    id = db.Column(db.Integer(), primary_key=True)


class GuardaRoupa(Base, BaseItem):

    __tablename__ = 'guardas_roupas'

    id = db.Column(db.Integer(), primary_key=True)
    numero_portas = db.Column(db.Integer())


class Sofa(Base, BaseItem):

    __tablename__ = 'sofas'

    id = db.Column(db.Integer(), primary_key=True)
    numero_lugares = db.Column(db.Integer())
