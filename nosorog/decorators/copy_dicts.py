import copy

from nosorog.decorators.base_decorator import BaseDecorator


class CopyDicts(BaseDecorator):
    """ The decorators for dicts copying. Does not work with @staticmethod."""

    def __init__(self, func, copy_method='copy_all', copy_type='copy'):
        super().__init__(func=func)
        self.copy_method = getattr(self, copy_method)
        self.copy_type = copy_type

    def __call__(self, obj, *args, **kwargs):
        new_args, new_kwargs = self.copy_method(*args, **kwargs)

        try:
            result = super().__call__(obj, *new_args, **new_kwargs)
        except Exception as ex:
            raise ex

        return result

    def copy_all(self, *args, **kwargs):
        new_args, _ = self.copy_args(*args)
        _, new_kwargs = self.copy_kwargs(**kwargs)

        return new_args, new_kwargs

    def copy_args(self, *args, **kwargs):
        new_args = [getattr(copy, self.copy_type)(ar) if type(ar) == dict else ar for ar in args]

        return new_args, kwargs

    def copy_kwargs(self, *args, **kwargs):
        try:
            new_kwargs = dict([(kwarg_name, getattr(copy, self.copy_type)(kwarg_item)) if type(kwarg_item) == dict else
                               (kwarg_name, kwarg_item) for kwarg_name, kwarg_item in kwargs.items()])
        except TypeError:
            new_kwargs = kwargs

        return args, new_kwargs

    @classmethod
    def shallow_args(cls, func):
        return cls(func, copy_method='copy_args', copy_type='copy')

    @classmethod
    def shallow_kwargs(cls, func):
        return cls(func, copy_method='copy_kwargs', copy_type='copy')

    @classmethod
    def shallow_all(cls, func):
        return cls(func, copy_method='copy_all', copy_type='copy')

    @classmethod
    def deep_args(cls, func):
        return cls(func, copy_method='copy_args', copy_type='deepcopy')

    @classmethod
    def deep_kwargs(cls, func):
        return cls(func, copy_method='copy_kwargs', copy_type='deepcopy')

    @classmethod
    def deep_all(cls, func):
        return cls(func, copy_method='copy_all', copy_type='deepcopy')
