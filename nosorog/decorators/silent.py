from nosorog.decorators.base_decorator import BaseDecorator
from nosorog.exceptions import NosorogWrongPlaceCallError, NosorogMangledNameError


class Silent(BaseDecorator):

    def __init__(self, func):
        super().__init__(func=func)

    def __call__(self, obj, *args, **kwargs):
        try:
            result = super().__call__(obj, *args, **kwargs)
        except Exception as ex:
            # catch Exception, compare it with DecoratorMessages, return None if message in list
            if isinstance(ex, (NosorogWrongPlaceCallError, NosorogMangledNameError)):
                result = None
            else:
                raise ex

        return result
