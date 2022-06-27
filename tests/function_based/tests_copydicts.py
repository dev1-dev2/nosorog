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
        def func(dict_a, dict_b=None):
            self.assertFalse(dict_a is self.item_dict, msg=self.msg)
            self.assertFalse(dict_b is self.item_dict, msg=self.msg)
            self.assertTrue(dict_a["key"] is self.item_dict["key"], msg=self.msg)
            if dict_b is not None:
                self.assertTrue(dict_b["key"] is self.item_dict["key"], msg=self.msg)

        func(self.item_dict, dict_b=self.item_dict)
        func(self.item_dict, dict_b=None)

    def test_copy_dict_decorator_deep_copy(self):
        @copy_dicts(deep_copy=True)
        def func(dict_a, dict_b=None):
            self.assertFalse(dict_a is self.item_dict, msg=self.msg)
            self.assertFalse(dict_b is self.item_dict, msg=self.msg)
            self.assertFalse(dict_a["key"] is self.item_dict["key"], msg=self.msg)
            if dict_b is not None:
                self.assertFalse(dict_b["key"] is self.item_dict["key"], msg=self.msg)

        func(self.item_dict, dict_b=self.item_dict)
        func(self.item_dict, dict_b=None)
