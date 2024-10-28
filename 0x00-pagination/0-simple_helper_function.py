#!/usr/bin/env python3
"""
0. Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    takes  two integer arguments page and page_size.
    return a tuple of size two containing a start index
    Args:
        page (int): current page
        page_size (int): number of items in a page
    Returns:
        (tuple): a tuple of the start and end index for the given page
    """
    nextPageStartIndex = page * page_size
    return nextPageStartIndex - page_size, nextPageStartIndex
