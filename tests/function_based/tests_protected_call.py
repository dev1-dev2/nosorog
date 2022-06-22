import os
import unittest

from nosorog.decorators.function_based import protected_call

from nosorog.exceptions.nosorog_wrong_place_call_error import NosorogWrongPlaceCallError
from nosorog.exceptions.mixins.nosorog_exception_messages import NosorogExceptionMessages

from tests.mixins.messages import Messages


class TestProtectedCall(unittest.TestCase, Messages):
    @protected_call(from_method='test_protected_call_decorator_allows_correct_call',
                    from_file=os.path.abspath(__file__))
    def func(self):
        return 1

    def test_protected_call_decorator_blocks_wrong_call(self):
        with self.assertRaises(NosorogWrongPlaceCallError, msg=self.msg_wrong_type) as context:
            self.func()
        self.assertTrue(NosorogExceptionMessages.wrong_place in str(context.exception),
                        msg="The protected_call decorator does not work with wrong call.")

    def test_protected_call_decorator_allows_correct_call(self):
        self.assertTrue(self.func() == 1, msg="The protected_call decorator does not work with correct call.")
