from nosorog.exceptions.nosorog_went_wrong_error import NosorogWentWrongError


class NosorogFakeError(NosorogWentWrongError):
    __module__ = Exception.__module__
