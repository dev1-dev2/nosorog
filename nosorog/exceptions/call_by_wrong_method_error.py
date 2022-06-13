from nosorog.exceptions.exception_template import ExceptionTemplate
from nosorog.exceptions.mixins.exception_messages import ExceptionMessages


class CallByWrongMethodError(ExceptionTemplate, ExceptionMessages):

    def __init__(self, message=None, errors=None, **kwargs):
        if message is not None:
            self.message = f'{self.protected_from_not_private_call} {message}'
        else:
            self.message = self.protected_from_not_private_call
        super(CallByWrongMethodError, self).__init__(message=self.message, errors=errors, **kwargs)
