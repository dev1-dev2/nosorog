import inspect

from nosorog.decorators.base_protect import BaseProtect
from nosorog.decorators.metaclasses.protected_call_meta import ProtectedCallMeta
from nosorog.exceptions import NosorogWentWrongError, NosorogFakeError, NosorogSplitAccessException


class ProtectedCall(BaseProtect, metaclass=ProtectedCallMeta):
    regexp_tmpl = r"( self)*(\.)({function_name})\("

    def __init__(self, *, func, attrs=None, protection_method=None):
        super().__init__(func=func, attrs=attrs, protection_method=protection_method)

    def __call__(self, obj, *args, **kwargs):

        fn = inspect.stack()

        self.set_regexp(
            function_name=self.func.__name__
        )

        func, message = self.get_props(self.protection_method)

        try:
            raise super(ProtectedCall, self)._BaseProtect__search_caller(fn, func)(message)
        except NosorogSplitAccessException:
            kwargs = dict()
        except NosorogFakeError:
            pass

        try:
            result = self.func(obj, *args, **kwargs)
        except Exception as ex:
            raise NosorogWentWrongError(str(ex))

        return result
