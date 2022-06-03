# Nosorog
## Introdaction

An assertive security framework.

## Installing

`pip install nosorog`
## How to use

`from nosorog.decorators import *`

**Decorator types**

`copy_dicts(deep_copy=bool)` make a copy of `dicts` in `args`.

`protect_private(allowed_list=list)` make `_Class__private_method()` impossible
    `allowed_list` it is `str` names of method which you can call the private method from.
                 also support `'self'` (`str`) for calls from same object only.

`protected_call(from_method=str, from_file=str)` make the attack by the file injection impossible.

`protect_ids(id_names=[str])` trying to convert id to `int` or throw Exception.

## Tests
This library has test suite.