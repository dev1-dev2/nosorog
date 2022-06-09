# Nosorog
## Introdaction

An assertive security library.

## Installing

`pip install nosorog`

## Testing

```
cd /path/to/lib/
python3 -m unittest discover
```

## How to use

`from nosorog.decorators import *`

**Decorator types**

`copy_dicts(deep_copy=bool)` make a copy of `dicts` in `args`.

`protect_private(allowed_list=list)` make `_Class__private_method()` impossible
    `allowed_list` it is `str` names of method which you can call the private method from.
                 also support `'self'` (`str`) for calls from same object only.

`protected_call(from_method=str, from_file=str)` make the attack by the file injection impossible.

`protect_ids(id_names=[str])` trying to convert id to `int` or throw Exception.

## Examples

### Private methods

Usage of dunder methods ( `__method()` ) protects the code avoiding direct access to the method.

```
class Example:
    def __get_data(self):
        return 1

>>> Example().__get_data()  # AttributeError: 'Example' object has no attribute '__get_data'
```
But it is possible to use the name mangling.
```
>>> Example()._Example__get_data()  # 1
```
Nosorog provides simple and pushy way to protect the dunder method.
```
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
```
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
attack by File Injection. With the help of the Nosorog library it is possible to specify the places from which the 
method can be called.
```
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

In the projects where the undefined number of dicts can be passed in args and kwargs, it is possible to make a deep copy 
of each if needed.
```
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
```
class Example:
    @protect_ids(id_names=['user_id', 'pk'])
    def some_method(user_id=None, pk=None)
        pass
```

Possible `Exceptions`
```
@protect_ids(id_names=['user_id', dict()])
>>> Example().some_method(user_id='1')  # TypeError: Wrong format of id_names in decorator. Must be list of str.

@protect_ids(id_names=['user_id', 'pk'])
>>> Example().some_method(user_id=1.234, pk='text_id')  # TypeError: Received the ids of wrong type.
```
