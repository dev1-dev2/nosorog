class NosorogWentWrongErrorMeta(type):

    @property
    def subclasses_tuple(cls):
        subclasses = cls.__subclasses__()
        return tuple(subclasses)
