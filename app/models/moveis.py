from . import db, Base, BaseItem


class BalcaoCooktop(Base, BaseItem):

    __tablename__ = 'balcoes_cooktop'

    id = db.Column(db.Integer(), primary_key=True)
