#!/usr/bin/env python3
"""
This module contains an async generator that yields
random numbers between 0 and 10 every second for 10 seconds.
"""

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """
    This function is an async generator that yields
    random numbers between 0 and 10 every second for 10 seconds.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
