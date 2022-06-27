def throw_exception(exc_type, with_msg=False):
    try:
        if with_msg:
            raise Exception('Test message.')
        else:
            raise Exception
    except Exception as ex:
        raise exc_type(original_exc=ex)
