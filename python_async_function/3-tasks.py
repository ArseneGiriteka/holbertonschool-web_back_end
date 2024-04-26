#!/usr/bin/env python3
"""
this is a special module that create and return a task
it will take a int value as argument
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    task_wait_random function
    max_delay integer argument
    return a Task Object
    """
    return asyncio.create_task(wait_random(max_delay))
