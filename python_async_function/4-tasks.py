#!/usr/bin/env python3
"""
Execute coroutines simultanously and implements an asynchronous
routine task_wait_n
that has two arguments n and max_delay
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_n function
    max_delay integer
    return a List of float numbers
    """
    result = [task_wait_random(max_delay) for i in range(n)]
    delays = []
    for task in result:
        delay = await task
        delays.append(delay)

    return delays
