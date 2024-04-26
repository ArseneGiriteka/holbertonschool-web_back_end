#!/usr/bin/env python3
"""
This module implements a coroutine named async_generator that has no
arguments and yield a random number between 0 and 10 after waiting 1 second
"""
import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    async_generator function
    no arguments
    return a Generator
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
