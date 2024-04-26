#!/usr/bin/env python3
"""
this module implements a method that get back random
numbers gereted by the asynchronous random numbers generator
"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension function
    no arguments
    return List of floats
    """
    return [i async for i in async_generator()]
