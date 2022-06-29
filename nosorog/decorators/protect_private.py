import inspect

from nosorog.decorators.base_protect import BaseProtect
from nosorog.decorators.metaclasses.protect_private_meta import ProtectPrivateMeta
from nosorog.exceptions import NosorogWentWrongError, NosorogFakeError


class ProtectPrivate(BaseProtect, metaclass=ProtectPrivateMeta):
    regexp_tmpl = r"( self)*(\.)(_{class_name})*({function_name})\("

    def __init__(self, *, func, attrs=None, protection_method=None):
        super().__init__(func=func, attrs=attrs, protection_method=protection_method)

    def __call__(self, obj, *args, **kwargs):

        fn = inspect.stack()

        self.set_regexp(
            class_name=obj.__class__.__name__,
            function_name=self.func.__name__
        )

        func, message = self.get_props(self.protection_method)

        try:
            raise self._BaseProtect__search_caller(fn, func)(message)
        except NosorogFakeError:
            pass

        try:
            result = self.func(obj, *args, **kwargs)
        except Exception as ex:
            raise NosorogWentWrongError(str(ex))

        return result
