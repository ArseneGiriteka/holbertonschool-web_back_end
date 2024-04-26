#!/usr/bin/env python3
"""
this module implements a function that count the runtime
of a routine and accepts two integer and return the runtime
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time function
    n integer
    max_delay integer
    return float number of seconds
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    return float((end - start) / n)
