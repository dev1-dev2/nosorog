from nosorog.exceptions.nosorog_went_wrong_error import NosorogWentWrongError


class NosorogTypeError(NosorogWentWrongError, TypeError):
    __module__ = Exception.__module__
