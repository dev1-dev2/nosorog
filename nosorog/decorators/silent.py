from nosorog.decorators.base_decorator import BaseDecorator
from nosorog.exceptions import NosorogWrongPlaceCallError, NosorogMangledNameError


class Silent(BaseDecorator):

    def __init__(self, func, exceptions=None):
        exceptions = exceptions or ()
        self.exceptions = (NosorogWrongPlaceCallError, NosorogMangledNameError, *exceptions)
        super().__init__(func=func)

    def __call__(self, obj, *args, **kwargs):
        try:
            result = super().__call__(obj, *args, **kwargs)
        except Exception as ex:
            # catch Exception, compare it with DecoratorMessages, return None if message in list
            if isinstance(ex, self.exceptions):
                result = None
            else:
                raise ex

        return result

    @classmethod
    def include(cls, exceptions):
        return lambda func: cls(func, exceptions)
