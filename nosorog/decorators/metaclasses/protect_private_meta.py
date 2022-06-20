class ProtectPrivateMeta(type):

    @property
    def one_obj(cls):
        return lambda func: cls(func=func, protection_method='block_if_not_self')

    @property
    def block_mangled_call(cls):
        return lambda func: cls(func=func, protection_method='block_if_mangled')
