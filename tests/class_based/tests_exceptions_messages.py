import unittest
from nosorog.exceptions import NosorogTypeError, NosorogWrongPlaceCallError, NosorogWentWrongError, \
    NosorogMangledNameError
from tests.testcases.class_based.exception_messages import throw_exception


class TestExceptionMessages(unittest.TestCase):
    def test_mangled_name_error_with_no_message(self):
        with self.assertRaises(NosorogMangledNameError, msg="Wrong type of Exception raised.") as context:
            throw_exception(NosorogMangledNameError)
        self.assertTrue('No especial message provided.' in str(context.exception), msg="Wrong Exception message.")
    
    def test_went_wrong_error_with_no_message(self):
        with self.assertRaises(NosorogWentWrongError, msg="Wrong type of Exception raised.") as context:
            throw_exception(NosorogWentWrongError)
        self.assertTrue('Something broken. The original exception was: "Exception"' in str(context.exception),
                        msg="Wrong Exception message.")
    
    def test_wrong_place_call_error_no_message(self):
        with self.assertRaises(NosorogWrongPlaceCallError, msg="Wrong type of Exception raised.") as context:
            throw_exception(NosorogWrongPlaceCallError)
        self.assertTrue('Protected method can be called from specified places only. The original exception was: '
                        '"Exception"' in str(context.exception), msg="Wrong Exception message.")
    
    def test_type_error_no_message(self):
        with self.assertRaises(NosorogTypeError, msg="Wrong type of Exception raised.") as context:
            throw_exception(NosorogTypeError)
        self.assertTrue('No especial message provided. The original exception was: "Exception"'
                        in str(context.exception), msg="Wrong Exception message.")

    def test_mangled_name_error_with_custom_message(self):
        with self.assertRaises(NosorogMangledNameError, msg="Wrong type of Exception raised.") as context:
            throw_exception(NosorogMangledNameError, with_msg=True)
        self.assertTrue('No especial message provided.' in str(context.exception), msg="Wrong Exception message.")

    def test_went_wrong_error_with_custom_message(self):
        with self.assertRaises(NosorogWentWrongError, msg="Wrong type of Exception raised.") as context:
            throw_exception(NosorogWentWrongError, with_msg=True)
        print(str(context.exception))
        self.assertTrue('Something broken. The original exception was: "Exception: Test message."'
                        in str(context.exception), msg="Wrong Exception message.")

    def test_wrong_place_call_error_custom_message(self):
        with self.assertRaises(NosorogWrongPlaceCallError, msg="Wrong type of Exception raised.") as context:
            throw_exception(NosorogWrongPlaceCallError, with_msg=True)
        self.assertTrue('Protected method can be called from specified places only. The original exception was: '
                        '"Exception: Test message."' in str(context.exception), msg="Wrong Exception message.")

    def test_type_error_custom_message(self):
        with self.assertRaises(NosorogTypeError, msg="Wrong type of Exception raised.") as context:
            throw_exception(NosorogTypeError, with_msg=True)
        self.assertTrue('No especial message provided. The original exception was: "Exception: Test message."'
                        in str(context.exception), msg="Wrong Exception message.")
