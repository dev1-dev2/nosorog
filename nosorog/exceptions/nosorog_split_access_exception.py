from nosorog.exceptions.nosorog_went_wrong_error import NosorogWentWrongError


class NosorogSplitAccessException(NosorogWentWrongError):
    __module__ = Exception.__module__

    def __init__(self, message=None, *, original_exc=None, errors=None, **kwargs):
        super(NosorogSplitAccessException, self).__init__(message=message, original_exc=original_exc,
                                                          errors=errors, **kwargs)
