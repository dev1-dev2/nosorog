from nosorog.decorators.metaclasses.base_protect_meta import BaseProtectMeta


class ProtectedCallMeta(BaseProtectMeta):

    def split(cls, methods):
        return lambda func: cls(func=func, attrs=methods, protection_method='split')
