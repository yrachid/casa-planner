from . import db, Base


class Bairro(Base):

    __tablename__ = 'bairros'

    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String())
    e_perigoso = db.Column(db.Boolean())


class Imovel(Base):

    __tablename__ = 'imoveis'

    id = db.Column(db.Integer(), primary_key=True)
    tamanho = db.Column(db.Float())
    bairro_id = db.Column(db.Integer(), db.ForeignKey('bairros.id'))
    bairro = db.relationship('Bairro')
    valor_aluguel = db.Column(db.Float())
    valor_condominio = db.Column(db.Float())
    valor_iptu = db.Column(db.Float())
