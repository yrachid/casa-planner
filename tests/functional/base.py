from flask_testing import LiveServerTestCase
from splinter import Browser
from etc.config import TEST_BROWSER
from app import factory

class FunctionalTestBase(LiveServerTestCase):

    def create_app(self):
        app = factory('etc.config.TestConfig')
        return app

    def setUp(self):
        self.browser = Browser(TEST_BROWSER)

    def tearDown(self):
        self.browser.quit()
