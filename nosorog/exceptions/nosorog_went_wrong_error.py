from nosorog.exceptions.metaclasses.nosorog_went_wrong_error_meta import NosorogWentWrongErrorMeta


class NosorogWentWrongError(Exception, metaclass=NosorogWentWrongErrorMeta):
    # Base Exception of Nosorog

    __module__ = Exception.__module__

    def __init__(self, message='Something broken.', *, original_exc=None, errors=None, **kwargs):
        self.message = self.format_message(message=message, original_exc=original_exc)
        self.errors = errors
        self.payload = kwargs

    def __str__(self):
        return self.message or ''

    @staticmethod
    def format_message(message, original_exc):
        if not message and original_exc:
            message = 'No especial message provided.'
        if original_exc:
            message = '{message} The original exception was: "{exc_type}{divider}{exc_msg}"'.format(
                message=message,
                exc_type=original_exc.__class__.__name__,
                divider=": " * bool(str(original_exc)),
                exc_msg=str(original_exc)
            )
        else:
            message = message

        return message
