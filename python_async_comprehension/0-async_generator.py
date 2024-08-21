#!/usr/bin/env python3
import asyncio
import random
import typing
"""
asycncronous generator that takes no arguments
and yields 10 random numbers between 0 and 10
evry second
"""


async def async_generator() -> typing.AsyncGenerator[float, None]:
    """
    this is the implementation of the async generator
    it takas no arguments and yields 10 random numbers
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
