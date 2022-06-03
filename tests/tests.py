import os
import unittest
from nosorog.decorators import copy_dicts, protect_private, protected_call, protect_ids


class TestCopyDictDecorator(unittest.TestCase):

    item_dict = {
        "key": {
            "inner_key": 1
        }
    }

    msg = "The copy_dicts decorator does not work."

    def test_copy_dict_decorator_shallow_copy(self):
        @copy_dicts(deep_copy=False)
        def func(a, b=None):
            self.assertFalse(a is self.item_dict, msg=self.msg)
            self.assertFalse(b is self.item_dict, msg=self.msg)
            self.assertTrue(a["key"] is self.item_dict["key"], msg=self.msg)
            if b is not None:
                self.assertTrue(b["key"] is self.item_dict["key"], msg=self.msg)

        func(self.item_dict, b=self.item_dict)
        func(self.item_dict, b=None)

    def test_copy_dict_decorator_deep_copy(self):
        @copy_dicts(deep_copy=True)
        def func(a, b=None):
            self.assertFalse(a is self.item_dict, msg=self.msg)
            self.assertFalse(b is self.item_dict, msg=self.msg)
            self.assertFalse(a["key"] is self.item_dict["key"], msg=self.msg)
            if b is not None:
                self.assertFalse(b["key"] is self.item_dict["key"], msg=self.msg)

        func(self.item_dict, b=self.item_dict)
        func(self.item_dict, b=None)


class Messages:
    msg_wrong_type = "Wrong type of Exception raised."
    msg_wrong_exc = "Wrong Exception message."


class TestProtectIdsDecorator(unittest.TestCase, Messages):
    @protect_ids(id_names=['user_id', 'pk'])
    def func(self, user_id=None, pk=None):
        return user_id, pk

    def test_protect_ids_decorator_converts_to_int(self):
        user_id, pk = self.func(user_id=1, pk='2')
        self.assertTrue(isinstance(user_id, int), msg="id value converted wrong way.")
        self.assertTrue(isinstance(pk, int), msg="pk value converted wrong way.")

    def test_protect_ids_throws_exception_when_id_has_wrong_type(self):
        with self.assertRaises(Exception, msg=self.msg_wrong_type) as context:
            self.func(id='1.234', pk='text_id')
        self.assertTrue("Received the ids of wrong type." in str(context.exception), msg=self.msg_wrong_exc)


class A:
    var = 1

    @protect_private(allowed_list=['public_func'])
    def __func_1(self):
        return self.var

    @protect_private(allowed_list=['self', 'alter_func_2'])
    def __func_2(self):
        return self.var

    def public_func(self):
        return self.__func_1()

    def alter_func_1(self):
        return self.__func_1()

    def alter_func_2(self):
        return self.__func_2()


class B:
    def __init__(self, a):
        self.a = a


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
