import inspect
import re

from nosorog.decorators.nosorog_base_decorator import NosorogBaseDecorator
from nosorog.exceptions.mixins.nosorog_exception_messages import NosorogExceptionMessages
from nosorog.exceptions import NosorogMangledNameError, NosorogWrongPlaceCallError, NosorogWentWrongError, \
    NosorogFakeError, NosorogSplitAccessException


class BaseProtect(NosorogBaseDecorator):
    regexp_tmpl = None

    def __init__(self, *, func, attrs=None, protection_method=None):
        super().__init__(func=func)
        self.attrs = attrs
        self.protection_method = protection_method
        self.regexp = None

    def __call__(self, obj, *args, **kwargs):

        fn = inspect.stack()

        self.set_regexp(
            class_name=obj.__class__.__name__,
            function_name=self.func.__name__
        )

        func, message = self.get_props(self.protection_method)

        try:
            raise self.__search_caller(fn, func)(message)
        except NosorogFakeError:
            pass

        try:
            result = self.func(obj, *args, **kwargs)
        except Exception as ex:
            raise NosorogWentWrongError(str(ex))

        return result

    def get_props(self, prop_name):
        protection_props = {
            'block_if_not_self': (
                lambda item, method_: NosorogFakeError if method_.group().startswith(' self')
                else NosorogWrongPlaceCallError,
                NosorogExceptionMessages.use_self,
            ),
            'block_if_wrong_method': (
                lambda item, method_: NosorogFakeError if item.function == self.attrs
                else NosorogWrongPlaceCallError, None,
            ),
            'block_if_not_in_list': (
                lambda item, method_: NosorogFakeError if item.function in self.attrs
                else NosorogWrongPlaceCallError, None,
            ),
            'block_if_mangled': (
                lambda item, method_: NosorogFakeError if '.__' in method_.group()
                else NosorogMangledNameError, None,
            ),
            'split': (
                lambda item, method_: NosorogFakeError if item.function in self.attrs
                else NosorogSplitAccessException, None,
            ),
        }

        return protection_props.get(prop_name)

    def set_regexp(self, **kwargs):
        self.regexp = self.regexp_tmpl.format(
            **kwargs
        )

    def __search_caller(self, fn, func):
        try:
            exception_gen = (func(item, re.search(self.regexp, item.code_context[0])) for item in fn if
                             re.search(self.regexp, item.code_context[0]))
            exception_type = next(exception_gen)
            exception_gen.close()
        except StopIteration:
            raise NosorogWentWrongError("The method that called the decorated method was not found.")
        except Exception as ex:
            raise NosorogWentWrongError("Something wrong with iteration through call stack.", original_exc=ex)

        return exception_type
