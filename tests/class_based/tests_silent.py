from nosorog.exceptions import NosorogWrongPlaceCallError
from nosorog.exceptions.mixins.nosorog_exception_messages import NosorogExceptionMessages
from tests.testcases.class_based.silent import ExceptionThrower

import unittest


class TestSilentDecorator(unittest.TestCase):

    def test_silent_decorator_returns_none_when_catchable_exception(self):
        self.assertIsNone(ExceptionThrower().get_catchable_exception())

    def test_silent_decorator_bypass_not_nosorog_exception(self):
        with self.assertRaises(Exception, msg="Wrong type of Exception raised.") as context:
            ExceptionThrower().get_aloud_exception()
        self.assertTrue("This is not Nosorog Exception." in str(context.exception), msg="Wrong Exception message.")

    def test_silent_decorator_returns_none_when_included_exception(self):
        self.assertIsNone(ExceptionThrower().get_included_exception())

    def test_silent_decorator_bypass_excluded_exception(self):
        with self.assertRaises(NosorogWrongPlaceCallError, msg="Wrong type of Exception raised.") as context:
            ExceptionThrower().get_excluded_exception()
        self.assertTrue(NosorogExceptionMessages.wrong_place in str(context.exception), msg="Wrong Exception message.")

    def test_silent_decorator_bypass_method_execution(self):
        self.assertTrue(ExceptionThrower().get_data() == 1)
