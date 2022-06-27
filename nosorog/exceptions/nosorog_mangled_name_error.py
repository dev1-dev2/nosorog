from nosorog.exceptions.nosorog_went_wrong_error import NosorogWentWrongError
from nosorog.exceptions.mixins.nosorog_exception_messages import NosorogExceptionMessages


class NosorogMangledNameError(NosorogWentWrongError, NosorogExceptionMessages):
    __module__ = Exception.__module__

    def __init__(self, /, message=None, *, errors=None, **kwargs):
        self.message = self.format_message(message)
        self.errors = errors
        self.payload = kwargs

    def format_message(self, message):
        if not message:
            message = 'No especial message provided.'
        message = '{message}{divider}{custom_msg}'.format(
            message=self.mangled_call_blocked,
            divider=": " * bool(str(message)),
            custom_msg=message
        )

        return message
