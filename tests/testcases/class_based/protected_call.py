from nosorog.decorators.protected_call import ProtectedCall as protected_call  # TODO refactor


class ProtectedCallUsage:

    @protected_call.one_method('call_method')
    def method_1(self):
        return 1

    @protected_call.one_obj
    def method_2(self):
        return 1

    @protected_call.call_from(['call_method'])
    def method_3(self):
        return 1

    @protected_call.split(['call_method'])
    def method_4(self, *args, **kwargs):
        return args, kwargs

    def call_method(self, *args, **kwargs):
        # does not work with getattr()
        if kwargs['method_name'] == 'method_4':
            result = self.method_4(*args, **kwargs)
        elif kwargs['method_name'] == 'method_1':
            result = self.method_1()
        elif kwargs['method_name'] == 'method_3':
            result = self.method_3()

        return result
