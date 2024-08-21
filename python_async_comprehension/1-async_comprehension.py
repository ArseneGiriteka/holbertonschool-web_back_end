#!/usr/bin/env python3

"""
This module contains an async comprehension that returns a list
of random numbers between 0 and 10 every second for 10 seconds.
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This function returns a list of random numbers between
    0 and 10 every second for 10 seconds.
    """
    return [i async for i in async_generator()]
