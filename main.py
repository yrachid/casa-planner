from app import factory
from app.views.users.list import UserListView
from app.models import db
import os

if __name__ == '__main__':

    try:
        app = factory(os.environ.get('SYRUP_CONFIG', 'DevelopmentConfig'))

        app.run()
    except Exception as error:
        print(str(error))
