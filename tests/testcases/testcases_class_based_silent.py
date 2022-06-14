from nosorog.decorators import silent
from nosorog.exceptions.nosorog_wrong_place_call_error import NosorogWrongPlaceCallError


class ExceptionThrower:

    @silent
    def get_catchable_exception(self):
        raise NosorogWrongPlaceCallError

    @silent
    def get_aloud_exception(self):
        raise Exception("This is not Nosorog Exception.")
