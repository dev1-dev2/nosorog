import unittest

from tests.testcases.class_based.copy_dicts import ProtectedDicts


class TestCopyDictsDecorator(unittest.TestCase):

    msg = "The copy_dicts decorator does not work."
    protected_dicts = ProtectedDicts()

    def test_copy_dict_decorator_shallow_copy_all(self):
        dict_a, dict_b = self.protected_dicts.method_1(self.protected_dicts.item_dict, dict_b=self.protected_dicts.item_dict)

        self.assertFalse(dict_a is self.protected_dicts.item_dict, msg=self.msg)
        self.assertFalse(dict_b is self.protected_dicts.item_dict, msg=self.msg)
        self.assertTrue(dict_a["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)
        self.assertTrue(dict_b["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)

    def test_copy_dict_decorator_shallow_copy_args(self):
        dict_a, dict_b = self.protected_dicts.method_2(self.protected_dicts.item_dict, dict_b=self.protected_dicts.item_dict)

        self.assertFalse(dict_a is self.protected_dicts.item_dict, msg=self.msg)
        self.assertTrue(dict_b is self.protected_dicts.item_dict, msg=self.msg)
        self.assertTrue(dict_a["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)
        self.assertTrue(dict_b["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)

    def test_copy_dict_decorator_shallow_copy_kwargs(self):
        dict_a, dict_b = self.protected_dicts.method_3(self.protected_dicts.item_dict, dict_b=self.protected_dicts.item_dict)

        self.assertTrue(dict_a is self.protected_dicts.item_dict, msg=self.msg)
        self.assertFalse(dict_b is self.protected_dicts.item_dict, msg=self.msg)
        self.assertTrue(dict_a["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)
        self.assertTrue(dict_b["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)

    def test_copy_dict_decorator_deep_copy_all(self):
        dict_a, dict_b = self.protected_dicts.method_4(self.protected_dicts.item_dict, dict_b=self.protected_dicts.item_dict)

        self.assertFalse(dict_a is self.protected_dicts.item_dict, msg=self.msg)
        self.assertFalse(dict_b is self.protected_dicts.item_dict, msg=self.msg)
        self.assertFalse(dict_a["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)
        self.assertFalse(dict_b["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)

    def test_copy_dict_decorator_deep_copy_args(self):
        dict_a, dict_b = self.protected_dicts.method_5(self.protected_dicts.item_dict, dict_b=self.protected_dicts.item_dict)

        self.assertFalse(dict_a is self.protected_dicts.item_dict, msg=self.msg)
        self.assertTrue(dict_b is self.protected_dicts.item_dict, msg=self.msg)
        self.assertFalse(dict_a["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)
        self.assertTrue(dict_b["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)

    def test_copy_dict_decorator_deep_copy_kwargs(self):
        dict_a, dict_b = self.protected_dicts.method_6(self.protected_dicts.item_dict, dict_b=self.protected_dicts.item_dict)

        self.assertTrue(dict_a is self.protected_dicts.item_dict, msg=self.msg)
        self.assertFalse(dict_b is self.protected_dicts.item_dict, msg=self.msg)
        self.assertTrue(dict_a["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)
        self.assertFalse(dict_b["key"] is self.protected_dicts.item_dict["key"], msg=self.msg)
