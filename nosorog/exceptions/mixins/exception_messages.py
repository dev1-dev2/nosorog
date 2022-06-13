class ExceptionMessages:
    protected_from_not_private_call = "This method protected from not private call."
    use_self = "This method can not be called from other object, use self instead."
    mangled_call_blocked = "This method can not be called by mangled name usage."
    bad_module = "Blocked import of vulnerable module."

    @classmethod
    def list(cls):
        return [
            cls.protected_from_not_private_call,
            cls.use_self,
            cls.mangled_call_blocked,
            cls.bad_module,
        ]
