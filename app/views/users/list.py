from app.views.base import ListView
from app.models.auth import User


class UserListView(ListView):

    def get_objects(self):
        return User.query.all()
