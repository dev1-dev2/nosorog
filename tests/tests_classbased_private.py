from tests.testcases.testcases_classbased_private import MangledNames
from nosorog.decorators.mixins.decorator_messages import DecoratorMessages

import unittest


class TestProtectPrivateDecorator(unittest.TestCase, DecoratorMessages):

    def test_protect_private_decorator_blocks_mangled_calls(self):
        # @protect_private.block_mangled_call
        with self.assertRaises(Exception, msg="Wrong type of Exception raised.") as context:
            MangledNames()._MangledNames__mangled_method_1()  # TODO change messages
        self.assertTrue(self.mangled_call_blocked in str(context.exception), msg="Wrong Exception message.")

    def test_protect_private_decorator_supports_not_mangled_calls(self):
        # @protect_private.block_mangled_call
        self.assertTrue(MangledNames().public_func_1() == 1, msg="Decorator does not work correctly.")

    def test_protect_private_decorator_blocks_not_allowed_methods_by_list_of_allowed(self):
        # @protect_private.call_from(methods=['public_func_2'])
        with self.assertRaises(Exception, msg="Wrong type of Exception raised.") as context:
            MangledNames().public_func_3()
        self.assertTrue(self.protected_from_not_private_call in str(context.exception), msg="Wrong Exception message.")

    def test_protect_private_decorator_supports_allowed_methods_by_list_of_allowed(self):
        # @protect_private.call_from(methods=['public_func_2'])
        self.assertTrue(MangledNames().public_func_2() == 1, msg="Decorator does not work correctly.")

    def test_protect_private_decorator_blocks_methods_except_of_one_method(self):
        # @protect_private.one_method('public_func_4')
        with self.assertRaises(Exception, msg="Wrong type of Exception raised.") as context:
            MangledNames().public_func_5()
        self.assertTrue(self.protected_from_not_private_call in str(context.exception), msg="Wrong Exception message.")

    def test_protect_private_decorator_supports_only_one_method(self):
        # @protect_private.one_method('public_func_4')
        self.assertTrue(MangledNames().public_func_4() == 1, msg="Decorator does not work correctly.")

    def test_protect_private_decorator_intercepts_exceptions_of_decorator_and_returns_none(self):
        # @protect_private.silent
        self.assertIsNone(MangledNames().public_func_6(), msg="Decorator does not work correctly.")
