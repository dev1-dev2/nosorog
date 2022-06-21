from nosorog.exceptions.metaclasses.nosorog_went_wrong_error_meta import NosorogWentWrongErrorMeta


class NosorogWentWrongError(Exception, metaclass=NosorogWentWrongErrorMeta):
    # Base Exception of Nosorog

    __module__ = Exception.__module__

    def __init__(self, message='Something broken.', *, errors=None, **kwargs):
        self.message = message
        self.errors = errors
        self.payload = kwargs

    def __str__(self):
        return self.message if self.message else ''
