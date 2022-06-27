from nosorog.decorators import copy_dicts


class ProtectedDicts:

    item_dict = {
        "key": {
            "inner_key": 1
        }
    }

    @copy_dicts.shallow_all
    def method_1(self, dict_a, dict_b=None):
        return dict_a, dict_b

    @copy_dicts.shallow_args
    def method_2(self, dict_a, dict_b=None):
        return dict_a, dict_b

    @copy_dicts.shallow_kwargs
    def method_3(self, dict_a, dict_b=None):
        return dict_a, dict_b

    @copy_dicts.deep_all
    def method_4(self, dict_a, dict_b=None):
        return dict_a, dict_b

    @copy_dicts.deep_args
    def method_5(self, dict_a, dict_b=None):
        return dict_a, dict_b

    @copy_dicts.deep_kwargs
    def method_6(self, dict_a, dict_b=None):
        return dict_a, dict_b
