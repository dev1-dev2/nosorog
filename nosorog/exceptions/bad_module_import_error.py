from nosorog.exceptions.exception_template import ExceptionTemplate
from nosorog.exceptions.mixins.exception_messages import ExceptionMessages


class BadModuleImportError(ExceptionTemplate, ExceptionMessages, Exception):
    def __init__(self, message=None, errors=None):
        if message:
            self.message = f'{self.bad_module} {message}'
        else:
            self.message = self.bad_module
        self.errors = errors
