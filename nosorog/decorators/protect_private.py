import inspect
import re

from nosorog.decorators.nosorog_base_decorator import NosorogBaseDecorator
from nosorog.exceptions.mixins.nosorog_exception_messages import NosorogExceptionMessages
from nosorog.exceptions import NosorogMangledNameError, NosorogWrongPlaceCallError
from nosorog.decorators.metaclasses.protect_private_meta import ProtectPrivateMeta


class ProtectPrivate(NosorogBaseDecorator, metaclass=ProtectPrivateMeta):
    __mangled_name = ''

    def __init__(self, func, attrs=None, protection_method=None):
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
        self.__mangled_name = '_{0}{1}'.format(
            obj.__class__.__name__, self.func.__name__
        )

        if self.protection_method:
            self.protection_method()

        try:
            result = super().__call__(obj, *args, **kwargs)
        except Exception as ex:
            raise ex

        return result

    @staticmethod
    def __search_caller(search_template, fn):
        try:
            items_gen = (item.function for item in fn if re.findall(search_template, item.code_context[0]))
            caller_name = next(items_gen)
            items_gen.close()
        except StopIteration as ex:
            caller_name = None

        return caller_name

    def __block_if_not_self(self):
        fn = inspect.stack()
        if not bool(self.__search_caller(r'self\.{name}\('.format(name=self.func.__name__), fn)):
            raise NosorogWrongPlaceCallError(NosorogExceptionMessages.use_self)

    def __block_if_not_in_list(self):
        fn = inspect.stack()
        if self.__search_caller(r'\.{name}\('.format(name=self.func.__name__), fn) not in self.attrs:
            raise NosorogWrongPlaceCallError

    def __block_if_wrong_method(self):
        fn = inspect.stack()
        if self.__search_caller(r'\.{name}\('.format(name=self.func.__name__), fn) != self.attrs:
            raise NosorogWrongPlaceCallError

    def __block_if_mangled(self):
        fn = inspect.stack()
        regexpr = r'\._[A-Za-z0-9_]+{}'.format(self.func.__name__)
        if self.__search_caller(regexpr, fn):
            raise NosorogMangledNameError
