from nosorog.exceptions.nosorog_went_wrong_error import NosorogWentWrongError
from nosorog.exceptions.mixins.nosorog_exception_messages import NosorogExceptionMessages


class NosorogBadModuleImportError(NosorogWentWrongError, NosorogExceptionMessages):
    __module__ = Exception.__module__

    def __init__(self, message=None, errors=None):
        if message:
            self.message = f'{self.bad_module} {message}'
        else:
            self.message = self.bad_module
        self.errors = errors
