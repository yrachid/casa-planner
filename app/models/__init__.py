from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declared_attr, declarative_base

db = SQLAlchemy()
Base = declarative_base()


class Loja(Base):

    __tablename__ = 'lojas'

    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String())

    def __repr__(self):
        return self.nome

    def __str__(self):
        return self.nome


class BaseItem():

    preco_parcelado = db.Column(db.Float())
    preco_a_vista = db.Column(db.Float())
    marca = db.Column(db.String())
    modelo = db.Column(db.String())
    altura = db.Column(db.Float())
    largura = db.Column(db.Float())
    comprimento = db.Column(db.Float())

    @declared_attr
    def loja_id(self):
        return db.Column(db.Integer(), db.ForeignKey('lojas.id'))

    @declared_attr
    def loja(self):
        return db.relationship('Loja')

    link_loja = db.Column(db.String())
