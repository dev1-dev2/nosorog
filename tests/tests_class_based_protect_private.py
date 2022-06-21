from tests.testcases.testcases_class_based_protect_private import MangledNames
from nosorog.exceptions.mixins.nosorog_exception_messages import NosorogExceptionMessages
from nosorog.exceptions import NosorogWrongPlaceCallError, NosorogMangledNameError

import unittest


class TestProtectPrivateDecorator(unittest.TestCase, NosorogExceptionMessages):

    def test_protect_private_decorator_blocks_mangled_calls(self):
        # @protect_private.block_mangled_call
        with self.assertRaises(NosorogMangledNameError, msg="Wrong type of Exception raised.") as context:
            MangledNames()._MangledNames__mangled_method_1()
        self.assertTrue(self.mangled_call_blocked in str(context.exception), msg="Wrong Exception message.")

    def test_protect_private_decorator_supports_not_mangled_calls(self):
        # @protect_private.block_mangled_call
        self.assertTrue(MangledNames().public_func_1() == 1, msg="Decorator does not work correctly.")

    def test_protect_private_decorator_blocks_not_allowed_methods_by_list_of_allowed(self):
        # @protect_private.call_from(methods=['public_func_2'])
        with self.assertRaises(NosorogWrongPlaceCallError, msg="Wrong type of Exception raised.") as context:
            MangledNames().public_func_3()
        self.assertTrue(self.wrong_place in str(context.exception), msg="Wrong Exception message.")

    def test_protect_private_decorator_supports_allowed_methods_by_list_of_allowed(self):
        # @protect_private.call_from(methods=['public_func_2'])
        self.assertTrue(MangledNames().public_func_2() == 1, msg="Decorator does not work correctly.")

    def test_protect_private_decorator_blocks_methods_except_of_one_method(self):
        # @protect_private.one_method('public_func_4')
        with self.assertRaises(NosorogWrongPlaceCallError, msg="Wrong type of Exception raised.") as context:
            MangledNames().public_func_5()
        self.assertTrue(self.wrong_place in str(context.exception), msg="Wrong Exception message.")

    def test_protect_private_decorator_supports_only_one_method(self):
        # @protect_private.one_method('public_func_4')
        self.assertTrue(MangledNames().public_func_4() == 1, msg="Decorator does not work correctly.")
