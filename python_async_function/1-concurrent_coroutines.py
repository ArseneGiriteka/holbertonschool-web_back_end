#!/usr/bin/env python3
"""
Execute coroutines simultanously and implements an asynchronous routine wait_n
that has two arguments n and max_delay
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n function
    max_delay integer
    return a List of float numbers
    """
    result = [wait_random(max_delay) for i in range(n)]
    delays = []
    for task in asyncio.as_completed(result):
        delay = await task
        delays.append(delay)

    return delays
