from app import factory
from flask_testing import TestCase

class UnitTestBase(TestCase):

    def create_app(self):
        app = factory('etc.config.TestConfig')
        self.client = app.test_client()
        return app
