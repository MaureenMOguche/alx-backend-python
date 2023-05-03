#!/usr/bin/env python3
"""
Module with function that measures the total execution time for an 
imported module wait_n(n, max_delay)
"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    returns total_time/n
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    return (end_time - start_time) / n


if __name__ == '__main__':
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
