from . import db, Base


class Bairro(Base):

    __tablename__ = 'bairros'

    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String())
    e_perigoso = db.Column(db.Boolean())

    def __repr__(self):
        return self.nome

    def __str__(self):
        return self.nome


class Imovel(Base):

    __tablename__ = 'imoveis'

    id = db.Column(db.Integer(), primary_key=True)
    tamanho = db.Column(db.Float())
    bairro_id = db.Column(db.Integer(), db.ForeignKey('bairros.id'))
    bairro = db.relationship('Bairro')
    valor_aluguel = db.Column(db.Float())
    valor_condominio = db.Column(db.Float())
    valor_iptu = db.Column(db.Float())
    numero_dormitorios = db.Column(db.Integer())
    tem_garagem = db.Column(db.Boolean())
    endereco = db.Column(db.String())
    link = db.Column(db.String())
    visitado = db.Column(db.Boolean())
    aprovado = db.Column(db.Boolean())
    andar = db.Column(db.Integer())
    nota = db.Column(db.Integer())
    codigo_imovel = db.Column(db.Integer())
    sol = db.Column(db.String())
    nivel_barulho = db.Column(db.Integer())
