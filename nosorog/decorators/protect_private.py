import inspect
import re

from nosorog.decorators.nosorog_base_decorator import NosorogBaseDecorator
from nosorog.exceptions.mixins.nosorog_exception_messages import NosorogExceptionMessages
from nosorog.exceptions import NosorogMangledNameError, NosorogWrongPlaceCallError, NosorogWentWrongError, \
                                    NosorogFakeError
from nosorog.decorators.metaclasses.protect_private_meta import ProtectPrivateMeta


class ProtectPrivate(NosorogBaseDecorator, metaclass=ProtectPrivateMeta):

    def __init__(self, *, func, attrs=None, protection_method=None):
        super().__init__(func=func)
        self.attrs = attrs
        self.protection_method = protection_method

    def __call__(self, obj, *args, **kwargs):

        fn = inspect.stack()

        self.regexp = r"( self)*(\.)(_{class_name})*({function_name})\(".format(
            class_name=obj.__class__.__name__,
            function_name=self.func.__name__
        )

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
        }

        func, message = protection_props.get(self.protection_method)

        try:
            raise self.__search_caller(fn, func)(message)
        except NosorogFakeError:
            pass

        try:
            result = super().__call__(obj, *args, **kwargs)
        except Exception as ex:
            raise NosorogWentWrongError(str(ex))

        return result

    def __search_caller(self, fn, func):
        try:
            items_gen = (func(item, re.search(self.regexp, item.code_context[0])) for item in fn if
                         re.search(self.regexp, item.code_context[0]))
            caller_name = next(items_gen)
            items_gen.close()
        except StopIteration:
            caller_name = None

        return caller_name
