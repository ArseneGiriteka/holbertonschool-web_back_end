#!/usr/bin/env python3
import asyncio
import random
import typing
"""This module contains an async generator that yields"""


async def async_generator() -> typing.AsyncGenerator[float, None]:
    """this function is an async generator that yields"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
