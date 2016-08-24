from . import db, Base


class GrupoDespensa(Base):

    __tablename__ = 'grupos_despensa'

    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String())

    def __repr__(self):
        return self.nome

    def __str__(self):
        return self.nome


class ItemDespensa(Base):

    __tablename__ = 'itens_despensa'

    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String())
    grupo_id = db.Column(db.Integer(), db.ForeignKey('grupos_despensa.id'))
    grupo = db.relationship('GrupoDespensa')
    estoque = db.Column(db.Integer())
    estoque_minimo = db.Column(db.Integer())
    marca = db.Column(db.String())
    ciclo = db.Column(
        db.Enum(
            'Sem ciclo',
            'Semanal',
            'Mensal',
            name='ciclos_despensa'
        )
    )
