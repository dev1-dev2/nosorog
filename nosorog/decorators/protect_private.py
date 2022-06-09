import inspect

from nosorog.decorators.base_decorator import BaseDecorator
from nosorog.decorators.mixins.decorator_messages import DecoratorMessages


class ProtectPrivate(BaseDecorator):
    mangled_name = ''

    def __init__(self, func, attrs=None, protection_method=None, handle_exception='base_handle_exception'):
        super().__init__(func=func)
        self.attrs = attrs
        if protection_method:
            self.protection_method = getattr(self, protection_method)
        self.handle_exception = getattr(self, handle_exception)

    def __call__(self, obj, *args, **kwargs):
        self.mangled_name = '_{0}{1}'.format(
            obj.__class__.__name__, self.func.__name__
        )

        if self.protection_method:
            self.protection_method()

        try:
            result = super().__call__(obj, *args, **kwargs)
        except Exception as ex:
            result = self.handle_exception(ex)

        return result

    @staticmethod
    def __base_method(args, kwargs):
        return args, kwargs

    @staticmethod
    def base_handle_exception(ex):
        raise ex

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
            raise Exception(DecoratorMessages.use_self)

    def block_if_not_in_list(self):
        fn = inspect.stack()
        if self.search_caller(f'.{self.func.__name__}(', fn) not in self.attrs:
            raise Exception(DecoratorMessages.protected_from_not_private_call)

    def block_if_wrong_method(self):
        fn = inspect.stack()
        if self.search_caller(f'.{self.func.__name__}(', fn) != self.attrs:
            raise Exception(DecoratorMessages.protected_from_not_private_call)

    def block_if_mangled(self):
        fn = inspect.stack()
        if self.search_caller(f'.{self.mangled_name}(', fn):
            raise Exception(DecoratorMessages.mangled_call_blocked)

    @staticmethod
    def block_silently(ex):
        # catch Exception, compare it with DecoratorMessages, return None if message in list
        if str(ex) in DecoratorMessages.list():
            return
        else:
            raise ex

    @classmethod
    def one_obj(cls, func):
        return cls(func=func, protection_method='block_if_not_self')

    @classmethod
    def one_method(cls, method):
        return lambda func: cls(func=func, attrs=method, protection_method='block_if_wrong_method')

    @classmethod
    def call_from(cls, methods):  # def from_methods
        return lambda func: cls(func=func, attrs=methods, protection_method='block_if_not_in_list')

    @classmethod
    def silent(cls, func):
        return cls(func=func, handle_exception='block_silently')

    @classmethod
    def block_mangled_call(cls, func):
        return cls(func=func, protection_method='block_if_mangled')
