from nosorog.decorators.function_based import protect_private


class Example1:
    var = 1

    @protect_private(allowed_list=['public_func'])
    def __func_1(self):
        return self.var

    @protect_private(allowed_list=['self', 'alter_func_2'])
    def __func_2(self):
        return self.var

    def public_func(self):
        return self.__func_1()

    def alter_func_1(self):
        return self.__func_1()

    def alter_func_2(self):
        return self.__func_2()


class Example2:
    def __init__(self, value):
        self.var_1 = value
