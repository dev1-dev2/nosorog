import inspect

from nosorog.decorators.base_decorator import BaseDecorator
from nosorog.exceptions.mixins.nosorog_exception_messages import NosorogExceptionMessages
from nosorog.exceptions import NosorogMangledNameError, NosorogWrongPlaceCallError


class ProtectPrivate(BaseDecorator):
    mangled_name = ''

    def __init__(self, func, attrs=None, protection_method=None):
        super().__init__(func=func)
        self.attrs = attrs
        if protection_method:
            self.protection_method = getattr(self, protection_method)

    def __call__(self, obj, *args, **kwargs):
        self.mangled_name = '_{0}{1}'.format(
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
    def search_caller(search_template, fn):
        try:
            caller_name = [item.function for item in fn if search_template in item.code_context[0]][0]
        except Exception:
            caller_name = None

        return caller_name

    def block_if_not_self(self):
        fn = inspect.stack()
        if not bool(self.search_caller(f'self.{self.func.__name__}(', fn)):
            raise NosorogWrongPlaceCallError(NosorogExceptionMessages.use_self)

    def block_if_not_in_list(self):
        fn = inspect.stack()
        if self.search_caller(f'.{self.func.__name__}(', fn) not in self.attrs:
            raise NosorogWrongPlaceCallError

    def block_if_wrong_method(self):
        fn = inspect.stack()
        if self.search_caller(f'.{self.func.__name__}(', fn) != self.attrs:
            raise NosorogWrongPlaceCallError

    def block_if_mangled(self):
        fn = inspect.stack()
        if self.search_caller(f'.{self.mangled_name}(', fn):
            raise NosorogMangledNameError

    @classmethod
    def one_obj(cls, func):
        return cls(func=func, protection_method='block_if_not_self')

    @classmethod
    def one_method(cls, method):
        return lambda func: cls(func=func, attrs=method, protection_method='block_if_wrong_method')

    @classmethod
    def call_from(cls, methods):
        return lambda func: cls(func=func, attrs=methods, protection_method='block_if_not_in_list')

    @classmethod
    def block_mangled_call(cls, func):
        return cls(func=func, protection_method='block_if_mangled')
