import inspect
import re

from nosorog.decorators.nosorog_base_decorator import NosorogBaseDecorator
from nosorog.exceptions.mixins.nosorog_exception_messages import NosorogExceptionMessages
from nosorog.exceptions import NosorogMangledNameError, NosorogWrongPlaceCallError, NosorogWentWrongError
from nosorog.decorators.metaclasses.protect_private_meta import ProtectPrivateMeta


class ProtectPrivate(NosorogBaseDecorator, metaclass=ProtectPrivateMeta):

    def __init__(self, *, func, attrs=None, protection_method=None):
        super().__init__(func=func)
        self.attrs = attrs

        if protection_method:
            methods = {
                'block_if_not_self': self.__block_if_not_self,
                'block_if_wrong_method': self.__block_if_wrong_method,
                'block_if_not_in_list': self.__block_if_not_in_list,
                'block_if_mangled': self.__block_if_mangled,
            }
            self.protection_method = methods.get(protection_method)

    def __call__(self, obj, *args, **kwargs):

        fn = inspect.stack()
        self.regexp = r"( self)*(\.)(_{class_name})*({function_name})\(".format(
            class_name=obj.__class__.__name__,
            function_name=self.func.__name__
        )
        self.protection_method(fn)

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

    def __block_if_not_self(self, fn):
        func = lambda item, method_: False if method_.group().startswith(' self') else True
        if self.__search_caller(fn, func):
            raise NosorogWrongPlaceCallError(NosorogExceptionMessages.use_self)

    def __block_if_not_in_list(self, fn):
        func = lambda item, method_: item.function
        if self.__search_caller(fn, func) not in self.attrs:
            raise NosorogWrongPlaceCallError

    def __block_if_wrong_method(self, fn):
        func = lambda item, method_: item.function
        if self.__search_caller(fn, func) != self.attrs:
            raise NosorogWrongPlaceCallError

    def __block_if_mangled(self, fn):
        func = lambda item, method_: False if '.__' in method_.group() else True
        if self.__search_caller(fn, func):
            raise NosorogMangledNameError
