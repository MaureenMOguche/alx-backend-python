#!/usr/bin/env python3
"""
    This module contains a function that takes 2 arguments (n and max_delay),
    and spawns another imported function (wait_random) n times with the
    specified max_delay
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    This function spawns wait_random n times with the specified max_delay
    and retuns a list of all theh delays in ascending order.
    """
    delays = []
    tasks = []

    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
