import copy

from nosorog.decorators.nosorog_base_decorator import NosorogBaseDecorator
from nosorog.decorators.metaclasses.copy_dicts_meta import CopyDictsMeta


class CopyDicts(NosorogBaseDecorator, metaclass=CopyDictsMeta):
    """ The decorators for dicts copying. Does not work with @staticmethod."""

    def __init__(self, *, func, copy_method='copy_all', copy_type='copy'):
        super().__init__(func=func)

        methods = {
            'copy_all': self.__copy_all,
            'copy_kwargs': self.__copy_kwargs,
            'copy_args': self.__copy_args,
        }

        self.copy_method = methods.get(copy_method)
        self.copy_type = copy_type

    def __call__(self, obj, *args, **kwargs):
        new_args, new_kwargs = self.copy_method(*args, **kwargs)

        try:
            result = super().__call__(obj, *new_args, **new_kwargs)
        except Exception as ex:
            raise ex

        return result

    def __copy_all(self, *args, **kwargs):
        new_args, _ = self.__copy_args(*args)
        _, new_kwargs = self.__copy_kwargs(**kwargs)

        return new_args, new_kwargs

    def __copy_args(self, *args, **kwargs):
        new_args = [getattr(copy, self.copy_type)(ar) if type(ar) == dict else ar for ar in args]

        return new_args, kwargs

    def __copy_kwargs(self, *args, **kwargs):
        try:
            new_kwargs = dict([(kwarg_name, getattr(copy, self.copy_type)(kwarg_item)) if type(kwarg_item) == dict else
                               (kwarg_name, kwarg_item) for kwarg_name, kwarg_item in kwargs.items()])
        except TypeError:
            new_kwargs = kwargs

        return args, new_kwargs
