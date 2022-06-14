from tests.testcases.testcases_class_based_silent import ExceptionThrower

import unittest


class TestSilentDecorator(unittest.TestCase):

    def test_silent_decorator_returns_none_when_catchable_exception(self):
        self.assertIsNone(ExceptionThrower().get_catchable_exception())

    def test_silent_decorator_bypass_not_nosorog_exception(self):
        with self.assertRaises(Exception, msg="Wrong type of Exception raised.") as context:
            ExceptionThrower().get_aloud_exception()
        self.assertTrue("This is not Nosorog Exception." in str(context.exception), msg="Wrong Exception message.")
