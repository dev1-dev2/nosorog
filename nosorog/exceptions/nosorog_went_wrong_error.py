class NosorogWentWrongError(Exception):
    # Base Exception of Nosorog

    __module__ = Exception.__module__

    def __init__(self, message='Something broken.', errors=None, **kwargs):
        self.message = message
        self.errors = errors
        self.payload = kwargs

    def __str__(self):
        return self.message if self.message else ''
