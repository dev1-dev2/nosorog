from nosorog.exceptions.nosorog_went_wrong_error import NosorogWentWrongError
from nosorog.exceptions.mixins.nosorog_exception_messages import NosorogExceptionMessages


class NosorogMangledNameError(NosorogWentWrongError, NosorogExceptionMessages):
    __module__ = Exception.__module__

    def __init__(self, message=None, errors=None, **kwargs):
        if message:
            self.message = f'{self.mangled_call_blocked} {message}'
        else:
            self.message = self.mangled_call_blocked
        super(NosorogMangledNameError, self).__init__(message=self.message, errors=errors, **kwargs)
