import unittest

from tests.testcases.class_based.copy_dicts import ProtectedDicts


class TestCopyDictsDecorator(unittest.TestCase):

    msg = "The copy_dicts decorator does not work."
    protected_dicts = ProtectedDicts()

    def test_copy_dict_decorator_shallow_copy_all(self):
        a, b = self.protected_dicts.method_1(self.protected_dicts.item_dict, b=self.protected_dicts.item_dict)

        self.assertFalse(a is self.protected_dicts.item_dict, msg=self.msg)
        self.assertFalse(b is self.protected_dicts.item_dict, msg=self.msg)
        self.assertTrue(a["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)
        self.assertTrue(b["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)

    def test_copy_dict_decorator_shallow_copy_args(self):
        a, b = self.protected_dicts.method_2(self.protected_dicts.item_dict, b=self.protected_dicts.item_dict)

        self.assertFalse(a is self.protected_dicts.item_dict, msg=self.msg)
        self.assertTrue(b is self.protected_dicts.item_dict, msg=self.msg)
        self.assertTrue(a["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)
        self.assertTrue(b["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)

    def test_copy_dict_decorator_shallow_copy_kwargs(self):
        a, b = self.protected_dicts.method_3(self.protected_dicts.item_dict, b=self.protected_dicts.item_dict)

        self.assertTrue(a is self.protected_dicts.item_dict, msg=self.msg)
        self.assertFalse(b is self.protected_dicts.item_dict, msg=self.msg)
        self.assertTrue(a["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)
        self.assertTrue(b["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)

    def test_copy_dict_decorator_deep_copy_all(self):
        a, b = self.protected_dicts.method_4(self.protected_dicts.item_dict, b=self.protected_dicts.item_dict)

        self.assertFalse(a is self.protected_dicts.item_dict, msg=self.msg)
        self.assertFalse(b is self.protected_dicts.item_dict, msg=self.msg)
        self.assertFalse(a["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)
        self.assertFalse(b["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)

    def test_copy_dict_decorator_deep_copy_args(self):
        a, b = self.protected_dicts.method_5(self.protected_dicts.item_dict, b=self.protected_dicts.item_dict)

        self.assertFalse(a is self.protected_dicts.item_dict, msg=self.msg)
        self.assertTrue(b is self.protected_dicts.item_dict, msg=self.msg)
        self.assertFalse(a["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)
        self.assertTrue(b["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)

    def test_copy_dict_decorator_deep_copy_kwargs(self):
        a, b = self.protected_dicts.method_6(self.protected_dicts.item_dict, b=self.protected_dicts.item_dict)

        self.assertTrue(a is self.protected_dicts.item_dict, msg=self.msg)
        self.assertFalse(b is self.protected_dicts.item_dict, msg=self.msg)
        self.assertTrue(a["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)
        self.assertFalse(b["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)
