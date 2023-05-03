#!/usr/bin/env python3
"""Contains function that takes an integer and returs an async Task"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """takes an integer max_delay and creates an async Task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
