import unittest

from nosorog.decorators.function_based import copy_dicts


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
