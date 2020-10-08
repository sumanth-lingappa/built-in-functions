
def myall(iterable):
    """ Implements built-in `all` function of Python"""
    """ Returns True only if all the elements in the iterable are truthy, else returns False """
    for item in iterable:
        if not item:
            return False
    return True