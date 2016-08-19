from unit.base import UnitTestBase
from hamcrest import assert_that, equal_to

class TestUnitTest(UnitTestBase):

    def test_that_should_pass(self):
        assert_that(1, equal_to(1))
