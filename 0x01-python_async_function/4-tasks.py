#!/usr/bin/env python3
"""Alters a function into a new task function"""

import asyncio
import random
from typing import List

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Alter the code from wait_n into a new async task
    """
    tasks = [
        asyncio.create_task(task_wait_random(max_delay)) for _ in range(n)
    ]
    return [await task for task in asyncio.as_completed(tasks)]
