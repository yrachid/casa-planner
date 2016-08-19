from functional.base import FunctionalTestBase
from hamcrest import assert_that, equal_to

class FunctionalTestCase(FunctionalTestBase):

    def test_should_pass(self):
        assert_that(1, equal_to(1))
