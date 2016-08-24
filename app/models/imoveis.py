from . import db, Base
from sqlalchemy.ext.hybrid import hybrid_property


class Bairro(Base):

    __tablename__ = 'bairros'

    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String())
    e_perigoso = db.Column(db.Boolean())

    def __repr__(self):
        return self.nome

    def __str__(self):
        return self.nome


class Imobiliaria(Base):

    __tablename__ = 'imobiliarias'

    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String())
    telefone = db.Column(db.Integer())
    link = db.Column(db.String())

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
    chuveiro = db.Column(db.String())
    tem_elevador = db.Column(db.Boolean())
    tem_portaria = db.Column(db.Boolean())
    tem_salao_festas = db.Column(db.Boolean())
    telefone = db.Column(db.String())
    parada_onibus = db.Column(db.Boolean())
    linha_onibus = db.Column(db.String())
    imobiliaria_id = db.Column(db.Integer(), db.ForeignKey('imobiliarias.id'))
    imobiliaria = db.relationship('Imobiliaria')
    mercado = db.Column(db.Boolean())
    farmacia = db.Column(db.Boolean())
    shopping = db.Column(db.Boolean())
    posto_gasolina = db.Column(db.Boolean())
    comentarios = db.Column(db.String())

    @hybrid_property
    def valor_total(self):
        aluguel = self.valor_aluguel or 0
        condominio = self.valor_condominio or 0
        iptu = self.valor_iptu or 0

        return aluguel + condominio + iptu
