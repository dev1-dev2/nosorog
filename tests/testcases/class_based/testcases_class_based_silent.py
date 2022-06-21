from nosorog.decorators import silent
from nosorog.exceptions.nosorog_wrong_place_call_error import NosorogWrongPlaceCallError


class ExceptionThrower:

    @silent
    def get_catchable_exception(self):
        raise NosorogWrongPlaceCallError

    @silent
    def get_aloud_exception(self):
        raise Exception("This is not Nosorog Exception.")

    @silent.include([TypeError])
    def get_included_exception(self):
        raise TypeError("This is not Nosorog Exception.")

    @silent.exclude([NosorogWrongPlaceCallError])
    def get_excluded_exception(self):
        raise NosorogWrongPlaceCallError

    @silent
    def get_data(self):
        return 1
