class NosorogExceptionMessages:
    protected_from_not_private_call = "This method protected from not private call."
    wrong_place = "Protected method can be called from specified methods only."
    use_self = "Protected method can not be called from other object, use self instead."
    mangled_call_blocked = "Use method`s dunder name instead."
    bad_module = "Blocked import of a vulnerable module."

    @classmethod
    def list(cls):
        return [
            cls.protected_from_not_private_call,
            cls.wrong_place,
            cls.use_self,
            cls.mangled_call_blocked,
            cls.bad_module,
        ]
