#!/usr/bin/env python3
import asyncio
import random
"""
asycncronous generator that takes no arguments
and yields 10 random numbers between 0 and 10
evry second
"""


async def async_generator():
    """
    this is the implementation of the async generator
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
