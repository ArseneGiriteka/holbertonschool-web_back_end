#!/usr/bin/env python3
"""
This module implements a coroutine named async_generator that has no
arguments and yield a random integer after wait 1 second
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """
    async_generator function
    no arguments
    return a Generator
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
