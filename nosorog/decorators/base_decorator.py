from functools import update_wrapper, partial


class BaseDecorator:

    def __init__(self, func):
        update_wrapper(self, func)
        self.func = func

    def __get__(self, obj, objtype):
        """Support instance methods."""
        return partial(self.__call__, obj)

    def __call__(self, obj, *args, **kwargs):
        try:
            result = self.func(obj, *args, **kwargs)
        except Exception as e:
            raise e
        else:
            return result

    @classmethod
    def get_decorator(cls, func):
        raise Exception("BaseDecorator and get_decorator method are not for direct usage, use inheritants instead.")
