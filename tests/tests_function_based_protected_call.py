import os
import unittest

from nosorog.decorators.function_based_decorators import protected_call
from tests.mixins.messages import Messages


class TestProtectedCall(unittest.TestCase, Messages):
    @protected_call(from_method='test_protected_call_decorator_allows_correct_call',
                    from_file=os.path.abspath(__file__))
    def func(self):
        return 1

    def test_protected_call_decorator_blocks_wrong_call(self):
        with self.assertRaises(ValueError, msg=self.msg_wrong_type) as context:
            self.func()
        self.assertTrue("This method protected." in str(context.exception), msg="The protected_call decorator does not "
                                                                                "work with wrong call.")

    def test_protected_call_decorator_allows_correct_call(self):
        self.assertTrue(self.func() == 1, msg="The protected_call decorator does not work with correct call.")
