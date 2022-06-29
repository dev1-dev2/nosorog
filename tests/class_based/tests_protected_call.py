from tests.testcases.class_based.protected_call import ProtectedCallUsage
from nosorog.exceptions.mixins.nosorog_exception_messages import NosorogExceptionMessages
from nosorog.exceptions import NosorogWrongPlaceCallError

import unittest


class TestProtectPrivateDecorator(unittest.TestCase, NosorogExceptionMessages):

    def test_protected_call_decorator_blocks_not_allowed_methods_by_list_of_allowed(self):
        # @protected_call.call_from(methods=['call_method'])  # TODO rename
        with self.assertRaises(NosorogWrongPlaceCallError, msg="Wrong type of Exception raised.") as context:
            ProtectedCallUsage().method_3()
        self.assertTrue(self.wrong_place in str(context.exception), msg="Wrong Exception message.")

    def test_protected_call_decorator_supports_allowed_methods_by_list_of_allowed(self):
        # @protected_call.call_from(methods=['call_method'])
        kwargs = dict()
        kwargs['method_name'] = 'method_1'
        self.assertTrue(ProtectedCallUsage().call_method(1, **kwargs) == 1, msg="Decorator does not work correctly.")

    def test_protected_call_decorator_blocks_methods_except_of_one_method(self):
        # @protected_call.one_method('call_method')
        with self.assertRaises(NosorogWrongPlaceCallError, msg="Wrong type of Exception raised.") as context:
            ProtectedCallUsage().method_1()
        self.assertTrue(self.wrong_place in str(context.exception), msg="Wrong Exception message.")

    def test_protected_call_decorator_supports_only_one_method(self):
        # @protected_call.one_method('call_method')
        kwargs = dict()
        kwargs['method_name'] = 'method_1'
        self.assertTrue(ProtectedCallUsage().call_method(1, **kwargs) == 1, msg="Decorator does not work correctly.")

    def test_protected_call_split_decorator_bypass_args_only_if_disallowed_method(self):
        # @protected_call.split(['call_method'])
        kwargs = dict()
        self.assertTrue(ProtectedCallUsage().method_4(1, **kwargs) == ((1,), {}),
                        msg="Decorator does not work correctly.")

    def test_protected_call_split_decorator_bypass_kwargs_only_if_allowed_method(self):
        # @protected_call.split(['call_method'])
        kwargs = dict()
        kwargs['method_name'] = 'method_4'
        self.assertTrue(ProtectedCallUsage().call_method(1, **kwargs) == ((1,), {'method_name': 'method_4'}),
                        msg="Decorator does not work correctly.")
