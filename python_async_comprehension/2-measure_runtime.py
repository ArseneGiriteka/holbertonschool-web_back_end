#!/usr/bin/env python3
"""
This module implements a runtime counter
of async_comprehension routine
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime function
    no arguments
    return float value
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return (end - start)
