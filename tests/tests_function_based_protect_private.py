import unittest

from tests.mixins.messages import Messages
from tests.testcases.testcases_function_based import B, A


class TestProtectPrivateDecorator(unittest.TestCase, Messages):
    b = B(A())

    def test_protect_private_decorator_blocks_outside_call(self):
        with self.assertRaises(Exception, msg=self.msg_wrong_type) as context:
            self.b.a._A__func_1()
        self.assertTrue("This method protected from not private call." in str(context.exception),
                        msg=self.msg_wrong_exc)

    def test_protect_private_decorator_blocks_not_allowed_list_func_name(self):
        with self.assertRaises(Exception, msg=self.msg_wrong_type) as context:
            self.b.a.alter_func_1()
        self.assertTrue("This method protected from not private call." in str(context.exception),
                        msg=self.msg_wrong_exc)

    def test_protect_private_decorator_bypass_allowed_list_func_name(self):
        self.assertTrue(self.b.a.public_func() == self.b.a.var, msg="The decorator does not bypass allowed methods.")

    def test_protect_private_decorator_bypass_allowed_list_with_self(self):
        self.assertTrue(self.b.a.alter_func_2() == self.b.a.var, msg="The decorator does not bypass methods with self.")
