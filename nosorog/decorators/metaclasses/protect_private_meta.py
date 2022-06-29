from nosorog.decorators.metaclasses.base_protect_meta import BaseProtectMeta


class ProtectPrivateMeta(BaseProtectMeta):

    @property
    def block_mangled_call(cls):
        return lambda func: cls(func=func, protection_method='block_if_mangled')
