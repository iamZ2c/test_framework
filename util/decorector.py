from functools import wraps
from unittest import TestCase, skipIf


# 本模块是处理case之间的依赖关系 6-3
class DependencyError(Exception):
    def __init__(self, _type=0):
        self._type = _type

    def __str__(self):
        if self._type == 0:
            return f'Dependency name of test os required!!!'
        elif self._type == 1:
            return f'Dependency name of test can not the case self!!!'


def depend(case=''):
    if not case:
        raise DependencyError
    _mark = []

    def warps_func(func):
        @wraps(func)
        def inner_func(self: TestCase()):
            if case == func.__name__:
                raise DependencyError(1)
            _r = self._outcome.result
            # 三组数据都是元组('name','reason')
            _f, _e, _s = _r.failures, _r.errors, _r.skipped

            if not (_f, _e, _r):
                func(self)

            if _f:
                _mark.extend([fail[0] for fail in _f])

            if _e:
                _mark.extend([error[0] for error in _e])

            if _s:
                _mark.extend([skipp[0] for skipp in _s])

            skipIf(
                case in str(_mark),
                f'The pre-depend case:{case} has failed! Skip the specified'
            )(func)(self)

        return inner_func

    return warps_func
