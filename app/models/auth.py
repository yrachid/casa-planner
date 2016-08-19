from . import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)


class Role(db.Model):

    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)


roles_users = db.Table(
    'roles_users',
    db.Column(
        'user_id',
        db.Integer(),
        db.ForeignKey('users.id')
    ),
    db.Column(
        'role_id',
        db.Integer(),
        db.ForeignKey('roles.id')
    )
)
