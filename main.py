from app import factory
from app.views.users.list import UserListView
from app.models import db
import os

app = factory('DevelopmentConfig')

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(port=port)
