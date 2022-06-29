import sys
import types

from nosorog.decorators.nosorog_base_decorator import NosorogBaseDecorator
from nosorog.decorators.mixins.bad_modules_mixin import BadModulesMixin
from nosorog.exceptions import CallByWrongMethodError, CallByMangledNameError, BadModuleImportError


class BlockBadModules(BadModulesMixin):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            self.block()
            result = self.func(*args, **kwargs)
        except Exception as ex:
            raise ex
        return result

    # Warning! pickle or cPickle are NOT designed as safe/secure solution for serialization.
    # Warning! yaml can be used for serialization/deserialization of executable objects.

    def block(self):

        for module_name in self.bad_modules:
            tmpl = "{{n.__init__.__globals__[{module_name}].__name__}}" \
                .format(module_name=module_name)

            if tmpl.format(n=self.func):
                raise Exception
        # modulenames = set(sys.modules) & set(globals())
        # print(modulenames)

        # for name, val in globals().items():
        #     if isinstance(val, types.ModuleType):
        #         print(val.__name__)
        #         if val.__name__ in self.bad_modules:
        #             raise BadModuleImportError

        # for module_name in self.bad_modules:
        #     loaded = sys.modules.get(module_name, False)
        #     if not loaded:
        #         raise BadModuleImportError
