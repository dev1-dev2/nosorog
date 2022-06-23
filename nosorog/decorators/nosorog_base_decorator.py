from functools import update_wrapper, partial


class NosorogBaseDecorator:

    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __get__(self, obj, objtype):
        """Support instance methods."""
        return partial(self.__call__, obj)

    def __call__(self, obj, *args, **kwargs):
        try:
            result = self.func(obj, *args, **kwargs)
        except Exception as ex:
            raise ex
        else:
            return result
