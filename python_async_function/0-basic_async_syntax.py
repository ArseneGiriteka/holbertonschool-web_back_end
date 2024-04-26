#!/usr/bin/env python3
"""*
asynchronous function that waits form a random number of seconds
between zero and given default max number and return the number of
secondes delayed
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random function
    max_delay integer
    return float number
    """
    number = random.uniform(0, float(max_delay))
    await asyncio.sleep(number)
    return number
