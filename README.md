# Nosorog
## Introdaction

An assertive security library.

## Requirements

3.5 >= Python <= 3.10

## Installing

`pip install nosorog`

## Testing

```python
cd /path/to/lib/
python3 -m unittest discover
```

## How to use

### Exceptions

Exception | Default message |
--- | --- |
`NosorogMangledNameError` | "Use method`s dunder name instead." |
`NosorogWrongPlaceCallError` (1) | "Protected method can be called from specified methods only." | 
`NosorogWrongPlaceCallError` (2) | "Protected method can not be called from other object, use self instead." | 
`NosorogWentWrongError` | "Something broken." |
`NosorogTypeError` | child of `TypeError`. No especial message provided. |

It is possible to use a concatenation of predefined and custom messages:
```python
raise NosorogMangledNameError("Method __get accessible with _MangledName__get() call.")
# NosorogMangledNameError: "Use method`s dunder name instead. Method __get accessible with _MangledName__get() call."
```
But it is one exclusion:
`NosorogWrongPlaceCallError` uses the message `"Protected method can be called from specified methods only."` by default 
and or other instead:
```python
from nosorog.exceptions.mixins.nosorog_exception_messages import NosorogExceptionMessages

raise NosorogWrongPlaceCallError(NosorogExceptionMessages.use_self)
# NosorogExceptionMessages: "Protected method can not be called from other object, use self instead."
```
It is not concatenated.

### Full list of predefined messages

Attribute | Message
--- | --- |
`protected_from_not_private_call` | "This method protected from not private call."
`method_protected` | "This method protected."
`wrong_place` | "Protected method can be called from specified places only."
`use_self` | "Protected method can not be called from other object, use self instead."
`mangled_call_blocked` | "Use method`s dunder name instead."

### Class based decorators


To import class based decorators use:

```python
from nosorog.decorators import protect_private, copy_dicts, silent
```


Decorator | Description |
--- | ---
`@silent` | intercepts all the exceptions of `Nosorog` and returns `None` instead. |
`@silent.include(exceptions)` | same as above and list of provided exceptions to. |
--- | ---
`@protect_private.block_mangled_call` | protect of name mangling usage. |
`@protect_private.one_obj` | decorated method accessible with `self` usage only. |
`@protect_private.one_method("method_name")` | decorated method accessible from one method only. |
`@protect_private.call_from(methods)` | decorated method accessible from the methods provided in list only. |
--- | ---
`@copy_dicts` | makes shallow copy of all the dicts in `args` and `kwargs` |
`@copy_dicts.deep_args` | makes deep copy of all the dicts in `args` |
`@copy_dicts.deep_kwargs` | makes deep copy of all the dicts in `kwargs` |
`@copy_dicts.deep_all` | makes deep copy of all the dicts in `args` and `kwargs` |
`@copy_dicts.shallow_args` | makes shallow copy of all the dicts in `args` |
`@copy_dicts.shallow_kwargs` | makes shallow copy of all the dicts in `kwargs` |
`@copy_dicts.shallow_all` | makes shallow copy of all the dicts in `args` and `kwargs` |


### Function based decorators


To import function based decorators use:

```python
from nosorog.decorators.function_based_decorators import protect_private, copy_dicts, protect_ids, protected_call
```


Decorator | Description                                                                                                                                                                                                   |
--- |---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
`@protect_private(allowed_list=list)`  | make a call with `_Class__private_method()` impossible. `allowed_list` it is `str` names of method which you can call the private method from. also support `'self'` (`str`) for calls from same object only. |
`@protected_call(from_method=str, from_file=str)` | make the attack by the file injection impossible.                                                                                                                                                             |
`@copy_dicts(deep_copy=bool)` | make a copy of `dicts` in `args` and `kwargs`.                                                                                                                                                                |
`@protect_ids(id_names=[str])`| trying to convert id to `int` or throw `Exception`.                                                                                                                                                           |


## Examples

This explanation written for the function based decorators. Class based decorators works the same way with some differences
in the syntax. Read the full documentation on https://nosorog.readthedocs.io.
### Private methods

Usage of dunder methods ( `__method()` ) protects the code avoiding direct access to the method.

```python
class Example:
    def __get_data(self):
        return 1

>>> Example().__get_data()  # AttributeError: 'Example' object has no attribute '__get_data'
```
But it is possible to use the name mangling.
```python
>>> Example()._Example__get_data()  # 1
```
`Nosorog` provides simple and pushy way to protect the dunder method.
```python
class Example:
    @protect_private(allowed_list=['trusted_func'])
    def __get_data(self):
        return 1

class Trusted:
    @staticmethod
    def trusted_func():
        return Example()._Example__get_data()

>>> Example().__get_data()  # AttributeError: 'Example' object has no attribute '__get_data'
>>> Example()._Example__get_data()  # Exception: This method protected from not private call.
>>> Trusted()._Example__get_data()  # 1
```
Also, str `'self'` can be used as a list item to make impossible to call without `self`.
```python
class Example:
    @protect_private(allowed_list=['trusted_func', 'self'])
    def __get_data(self):
        return 1

    def trusted_func(self):
        return self.__get_data()


class Trusted:
    @staticmethod
    def trusted_func():
        return Example()._Example__get_data()

>>> Example().trusted_func()  # 1
>>> Trusted().trusted_func()  # Exception: This method can not be called from other object, use self instead.
```

### Localization of method call

Python does not provide an easy way to limit where the method can be called from. This makes it possible to conduct an
attack by File Injection. With the help of the `Nosorog` library it is possible to specify the places from which the 
method can be called.
```python
class Example:
    @protected_call(from_method='safe_method', from_file=os.path.abspath(__file__))
    def __get_data(self):
        return 1

class Trusted:
    # Place it to the same file as described in the decorator usage.
    def safe_method():
        return Example()._Example__get_data()  # 1
```
This is just a variation of the previous decorator.

### Protection of the dicts

In the projects where the undefined number of dicts can be passed in `args` and `kwargs`, it is possible to make a deep copy 
of each if needed.
```python
class Example:
    @copy_dicts(deep_copy=False)
    def some_method(self, *args, **kwargs):
        # now dicts are shallow copies
        pass
```
Use `@copy_dicts(deep_copy=True)` to make deep copies.

### Protection of ids

This method has been added just for fun.
It is converts all the ids in the list if possible or throws the `TypeError`.
```python
class Example:
    @protect_ids(id_names=['user_id', 'pk'])
    def some_method(user_id=None, pk=None)
        pass
```

Possible `Exceptions`
```python
@protect_ids(id_names=['user_id', dict()])
>>> Example().some_method(user_id='1')  # TypeError: Wrong format of id_names in decorator. Must be list of str.

@protect_ids(id_names=['user_id', 'pk'])
>>> Example().some_method(user_id=1.234, pk='text_id')  # TypeError: Received the ids of wrong type.
```
