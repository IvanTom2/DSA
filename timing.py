import timeit
import numpy as np
from functools import wraps
from copy import deepcopy
from typing import Callable, Tuple, Any
from tqdm import tqdm


class TimeGradation(object):
    grads = [
        (0.001, 5000),
        (0.01, 1000),
        (0.1, 100),
        (1, 50),
    ]

    def get_repetition_counts(self, exec_time: float) -> int:
        for grad in self.grads:
            if exec_time < grad[0]:
                return grad[1]
        return 0


def copy_dict(dictinary: dict) -> dict:
    keys = list(dictinary.keys())
    values = [deepcopy(dictinary[key]) for key in keys]

    return {x: y for x, y in zip(keys, values)}


def exec_func(func: Callable, *args, **kwargs) -> Tuple[Any, float]:
    _args = tuple(map(deepcopy, args)) if args else ()
    _kwargs = copy_dict(kwargs) if kwargs else {}

    start = timeit.default_timer()
    output = func(*_args, **_kwargs)
    exec_time = timeit.default_timer() - start

    return output, exec_time


def repeates_count(exec_time: float, min_repetitions: int) -> int:
    repetitions = TimeGradation().get_repetition_counts(exec_time)
    return max(repetitions, min_repetitions)


def repeater(min_repetitions: int = 10, max_repetitions: int = None):
    def timer(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            exec_times = []
            output, exec_time = exec_func(func, *args, **kwargs)
            exec_times.append(exec_time)

            repetitions = repeates_count(exec_time, min_repetitions)
            if max_repetitions is not None:
                repetitions = min(repetitions, max_repetitions)

            for _ in tqdm(range(repetitions - 1)):
                output, exec_time = exec_func(func, *args, **kwargs)
                exec_times.append(exec_time)

            output = func(*args, **kwargs)
            tmean = np.mean(exec_times)
            tmin = np.min(exec_times)

            print(func.__qualname__)
            print(f"Mean time = {tmean * 1000:.5f} ms")
            print(f"Min time  = {tmin * 1000:.5f} ms")
            print("\n")

            return output

        return wrapper

    return timer
