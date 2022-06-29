from dataclasses import dataclass

from nosorog.decorators.nosorog_base_decorator import NosorogBaseDecorator


class ProtectedDataclass(NosorogBaseDecorator):

    def __init__(self, decorated_class):
        self.decorated_class = decorated_class

    def __call__(self, obj, *args, **kwargs):
        try:
            protector = super().__call__(obj, *args, **kwargs)
        except Exception as ex:
            raise ex

        return protector
