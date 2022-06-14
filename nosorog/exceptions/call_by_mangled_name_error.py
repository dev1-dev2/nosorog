from nosorog.exceptions.exception_template import ExceptionTemplate
from nosorog.exceptions.mixins.exception_messages import ExceptionMessages


class CallByMangledNameError(ExceptionTemplate, ExceptionMessages):
    def __init__(self, message=None, errors=None, **kwargs):
        if message:
            self.message = f'{self.mangled_call_blocked} {message}'
        else:
            self.message = self.mangled_call_blocked
        super(CallByMangledNameError, self).__init__(message=self.message, errors=errors, **kwargs)
