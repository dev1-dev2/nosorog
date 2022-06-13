class ExceptionTemplate(Exception):

    __module__ = Exception.__module__

    def __init__(self, message='', errors=None, **kwargs):
        super().__init__(message)
        self.errors = errors
        self.payload = kwargs

    def __str__(self):
        return self.message if self.message else ''
