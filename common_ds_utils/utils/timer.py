import time
from datetime import datetime


def timed(func):
    """Decorator for timing function calls

    Args:
        func (function): function as input
    """
    def _wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(
            f"Completed {func.__name__} in {time.time() - start:.3f} sec"
        )
        return res

    return _wrapper


def get_current_time():
    """Generic method to get formatted current time

    Returns:
        str: formatted time
    """
    return "{:%Y_%m_%d_%H_%M_%S}".format(datetime.now())
