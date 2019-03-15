import time
import sys
from callhub.dbapi import FibSeriesDbio
from callhub.models import FibSeries


class StoreResult:
    def __init__(self):
        self.fibdb = FibSeriesDbio()


def timeit(method):

    def timed(*args, **kw):
        time_start = time.time()
        result = method(*args, **kw)
        num = [a for a in args]
        create_num(num[0], result, time.time()-time_start)
        return result

    return timed


def create_num(num, result, total_time):
    FibSeries.objects.get_or_create(
        num_key=num,
        defaults={
            'result': result,
            'exec_time': total_time
        }
    )


class recursionlimit:
    def __init__(self, limit):
        self.limit = limit
        self.old_limit = sys.getrecursionlimit()

    def __enter__(self):
        sys.setrecursionlimit(self.limit)

    def __exit__(self, type, value, tb):
        sys.setrecursionlimit(self.old_limit)
