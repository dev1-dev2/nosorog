from nosorog.decorators import silent
from nosorog.exceptions.call_by_wrong_method_error import CallByWrongMethodError


class ExceptionThrower:

    @silent
    def get_catchable_exception(self):
        raise CallByWrongMethodError

    @silent
    def get_aloud_exception(self):
        raise Exception("This is not Nosorog Exception.")
