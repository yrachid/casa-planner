from . import db, Base


class User(Base):

    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)


class Role(Base):

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
