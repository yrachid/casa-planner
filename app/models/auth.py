from . import db, Base
from sqlalchemy.ext.declarative import declared_attr


class User(Base):

    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)


class Role(Base):

    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)


class RolesUsers(Base):

    __tablename__ = 'roles_users'

    id = db.Column(db.Integer(), primary_key=True)

    @declared_attr
    def user_id(self):
        return db.Column(db.Integer(), db.ForeignKey('users.id'))

    @declared_attr
    def role_id(self):
        return db.Column(db.Integer(), db.ForeignKey('roles.id'))
