import unittest

from tests.mixins.messages import Messages
from tests.testcases.function_based.testcases import Example2, Example1

from nosorog.exceptions import NosorogWrongPlaceCallError
from nosorog.exceptions.mixins.nosorog_exception_messages import NosorogExceptionMessages


class TestProtectPrivateDecorator(unittest.TestCase, Messages):
    instance = Example2(Example1())

    def test_protect_private_decorator_blocks_outside_call(self):
        with self.assertRaises(NosorogWrongPlaceCallError, msg=self.msg_wrong_type) as context:
            self.instance.var_1._Example1__func_1()
        self.assertTrue(NosorogExceptionMessages.wrong_place in str(context.exception),
                        msg=self.msg_wrong_exc)

    def test_protect_private_decorator_blocks_not_allowed_list_func_name(self):
        with self.assertRaises(NosorogWrongPlaceCallError, msg=self.msg_wrong_type) as context:
            self.instance.var_1.alter_func_1()
        self.assertTrue(NosorogExceptionMessages.wrong_place in str(context.exception),
                        msg=self.msg_wrong_exc)

    def test_protect_private_decorator_bypass_allowed_list_func_name(self):
        self.assertTrue(self.instance.var_1.public_func() == self.instance.var_1.var,
                        msg="The decorator does not bypass allowed methods.")

    def test_protect_private_decorator_bypass_allowed_list_with_self(self):
        self.assertTrue(self.instance.var_1.alter_func_2() == self.instance.var_1.var,
                        msg="The decorator does not bypass methods with self.")
