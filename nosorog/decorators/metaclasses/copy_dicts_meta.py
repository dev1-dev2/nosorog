class CopyDictsMeta(type):
    @property
    def shallow_args(cls):
        return lambda func: cls(func, copy_method='copy_args', copy_type='copy')

    @property
    def shallow_kwargs(cls):
        return lambda func: cls(func, copy_method='copy_kwargs', copy_type='copy')

    @property
    def shallow_all(cls):
        return lambda func: cls(func, copy_method='copy_all', copy_type='copy')

    @property
    def deep_args(cls):
        return lambda func: cls(func, copy_method='copy_args', copy_type='deepcopy')

    @property
    def deep_kwargs(cls):
        return lambda func: cls(func, copy_method='copy_kwargs', copy_type='deepcopy')

    @property
    def deep_all(cls):
        return lambda func: cls(func, copy_method='copy_all', copy_type='deepcopy')
