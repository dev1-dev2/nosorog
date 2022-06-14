from nosorog.decorators import protect_private


class MangledNames:
    __var = 1

    @protect_private.block_mangled_call
    def __mangled_method_1(self):
        return self.__var

    @protect_private.call_from(methods=['public_func_2'])
    def __mangled_method_2(self):
        return self.__var

    @protect_private.one_method('public_func_4')
    def __mangled_method_3(self):
        return self.__var

    def public_func_1(self):
        return self.__mangled_method_1()

    def public_func_2(self):
        return self.__mangled_method_2()

    def public_func_3(self):
        return self.__mangled_method_2()

    def public_func_4(self):
        return self.__mangled_method_3()

    def public_func_5(self):
        return self.__mangled_method_3()
