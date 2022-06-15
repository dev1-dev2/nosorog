from nosorog.exceptions.nosorog_went_wrong_error import NosorogWentWrongError
from nosorog.exceptions.mixins.nosorog_exception_messages import NosorogExceptionMessages


class NosorogWrongPlaceCallError(NosorogWentWrongError, NosorogExceptionMessages):
    __module__ = Exception.__module__

    def __init__(self, message=None, errors=None, **kwargs):
        if message is not None:
            self.message = message
        else:
            self.message = self.wrong_place
        super(NosorogWrongPlaceCallError, self).__init__(message=self.message, errors=errors, **kwargs)
