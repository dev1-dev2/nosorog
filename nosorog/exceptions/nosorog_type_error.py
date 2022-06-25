from nosorog.exceptions.nosorog_went_wrong_error import NosorogWentWrongError


class NosorogTypeError(NosorogWentWrongError, TypeError):
    __module__ = Exception.__module__

    def __init__(self, /, message=None, *, original_exc=None, errors=None, **kwargs):
        message = message or self.wrong_place
        super(NosorogTypeError, self).__init__(message=message, original_exc=original_exc,
                                               errors=errors, **kwargs)
