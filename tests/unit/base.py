from app import factory
from flask_testing import TestCase


class UnitTestBase(TestCase):

    def create_app(self):
        app = factory('TestConfig')
        self.client = app.test_client()
        return app
