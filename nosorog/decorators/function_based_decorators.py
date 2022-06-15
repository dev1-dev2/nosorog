import copy
import inspect

from nosorog.exceptions import NosorogTypeError, NosorogWrongPlaceCallError
from nosorog.exceptions.mixins.nosorog_exception_messages import NosorogExceptionMessages


def copy_dicts(deep_copy=False):
    def decorator(func):
        def wrap(*args, **kwargs):
            copy_method = "deepcopy" if deep_copy is True else "copy"
            new_args = [getattr(copy, copy_method)(ar) if type(ar) == dict else ar for ar in args]

            try:
                new_kwargs = dict([(kwarg_name, getattr(copy, copy_method)(kwarg_item)) if type(kwarg_item) == dict else
                                   (kwarg_name, kwarg_item) for kwarg_name, kwarg_item in kwargs.items()])
            except TypeError:
                new_kwargs = kwargs
            result = func(*new_args, **new_kwargs)

            return result

        return wrap

    return decorator


def protect_ids(id_names=None):
    # Convert all the items in id_names to int or throw TypeError
    def decorator(func):
        def wrap(*args, **kwargs):
            if id_names and isinstance(id_names, list) and set([type(name) for name in id_names]) != {str}:
                raise NosorogTypeError("Wrong format of id_names in decorator. Must be list of str.")
            if id_names:
                try:
                    new_kwargs = dict([(kwarg_name, int(kwarg_item)) if kwarg_name in id_names else
                                       (kwarg_name, kwarg_item) for kwarg_name, kwarg_item in kwargs.items()])
                except Exception:
                    raise NosorogTypeError("Received the ids of wrong type.")
            else:
                new_kwargs = kwargs
            result = func(args, **new_kwargs)

            return result

        return wrap
    return decorator


def protect_private(allowed_list=None, silent=False):
    # Makes method not accessible from the method which not in allowed_list.
    # Return None instead of throwing Exception if silent is True
    def decorator(func):
        def wrap(*args, **kwargs):

            fn = inspect.stack()

            if allowed_list and 'self' in allowed_list and 'self.{}('.format(func.__name__) not in fn[1].code_context[0]:
                if silent:
                    return None
                raise NosorogWrongPlaceCallError(NosorogExceptionMessages.use_self)
            elif allowed_list and fn[1].function not in allowed_list:
                if silent:
                    return None
                raise NosorogWrongPlaceCallError(NosorogExceptionMessages.wrong_place)
            elif allowed_list is None:
                return None

            result = func(*args, **kwargs)

            return result

        return wrap

    return decorator


def protected_call(from_method=None, from_file=None):
    # limits the places where the method can be called from.
    def decorator(func):
        def wrapper(*args, **kwargs):
            fn = inspect.stack()
            if from_method is not None and fn[1].function != from_method:
                raise NosorogWrongPlaceCallError
            if from_file is not None and fn[1].filename != from_file:
                raise NosorogWrongPlaceCallError
            result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator
