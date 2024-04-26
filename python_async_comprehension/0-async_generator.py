#!/usr/bin/env python3
"""
This module implements a coroutine named async_generator that has no
arguments and yield a random integer after wait 1 second
this function is a good one
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator():
    """
    async_generator function
    no arguments
    return a Generator
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
