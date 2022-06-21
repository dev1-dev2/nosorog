class A:
    _A__var = 1
    __var_2 = 2

    def test_1(self):
        return self.__var

    def test_2(self):
        return self._A__var

    def test_3(self):
        return self.__var_2
