import unittest

from nosorog.decorators.function_based_decorators import protect_ids
from tests.mixins.messages import Messages


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
