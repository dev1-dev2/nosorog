import unittest

from tests.testcases.function_based.reasoning import A


class TestMangledNamesUsage(unittest.TestCase):

    def test_dunder_blocks_direct_access(self):
        # name mangling has a bug. It can not be checked with unittests package. Should be _A__var.
        with self.assertRaises(AttributeError,
                               msg="'A' object has no attribute '_TestMangledNamesUsage__var'") as context:
            a = A().__var
        self.assertTrue("'A' object has no attribute '_TestMangledNamesUsage__var'" in str(context.exception),
                        msg="Wrong message.")

    def test_dunder_supports_mangled_access_to_mangled_field(self):
        self.assertTrue(A()._A__var == 1)

    def test_dunder_supports_mangled_access_to_not_mangled_field(self):
        self.assertTrue(A()._A__var_2 == 2)

    def test_dunder_supports_mangled_access_to_mangled_field_with_self_usage(self):
        self.assertTrue(A().test_2() == 1)

    def test_dunder_supports_direct_access_to_mangled_field_with_self_usage(self):
        self.assertTrue(A().test_1() == 1)

    def test_dunder_supports_direct_access_to_not_mangled_field_with_self_usage(self):
        self.assertTrue(A().test_3() == 2)
