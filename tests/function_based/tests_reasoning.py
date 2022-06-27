import unittest

from tests.testcases.function_based.reasoning import Example


class TestMangledNamesUsage(unittest.TestCase):

    def test_dunder_blocks_direct_access(self):
        # name mangling has a bug. It can not be checked with unittests package. Should be _Example__var.
        with self.assertRaises(AttributeError,
                               msg="'Example' object has no attribute '_TestMangledNamesUsage__var'") as context:
            instance = Example().__var
        self.assertTrue("'Example' object has no attribute '_TestMangledNamesUsage__var'" in str(context.exception),
                        msg="Wrong message.")

    def test_dunder_supports_mangled_access_to_mangled_field(self):
        self.assertTrue(Example()._Example__var == 1)

    def test_dunder_supports_mangled_access_to_not_mangled_field(self):
        self.assertTrue(Example()._Example__var_2 == 2)

    def test_dunder_supports_mangled_access_to_mangled_field_with_self_usage(self):
        self.assertTrue(Example().test_2() == 1)

    def test_dunder_supports_direct_access_to_mangled_field_with_self_usage(self):
        self.assertTrue(Example().test_1() == 1)

    def test_dunder_supports_direct_access_to_not_mangled_field_with_self_usage(self):
        self.assertTrue(Example().test_3() == 2)
