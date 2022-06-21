from nosorog.decorators import copy_dicts


class ProtectedDicts:

    item_dict = {
        "key": {
            "inner_key": 1
        }
    }

    @copy_dicts.shallow_all
    def method_1(self, a, b=None):
        return a, b

    @copy_dicts.shallow_args
    def method_2(self, a, b=None):
        return a, b

    @copy_dicts.shallow_kwargs
    def method_3(self, a, b=None):
        return a, b

    @copy_dicts.deep_all
    def method_4(self, a, b=None):
        return a, b

    @copy_dicts.deep_args
    def method_5(self, a, b=None):
        return a, b

    @copy_dicts.deep_kwargs
    def method_6(self, a, b=None):
        return a, b
