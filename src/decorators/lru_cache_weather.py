"""
Well, bless your heart! This here's LRU caching - "Least Recently Used" -
sweeter than pecan pie. It's like Meemaw's recipe drawer: keeps the most
recent results handy, tosses out the old ones when it gets full as a tick.

The @lru_cache decorator works slicker than grease - first call does the
work, second call with same arguments serves up the saved result quicker
than sweet tea on a summer day. No need for duplicate API calls!
"""

from functools import lru_cache

import requests


@lru_cache(maxsize=128)
def get_weather(city):
    url = f"https://api.weatherapi.com/{city}"
    return requests.get(url, timeout=10).json()


print(get_weather("London"))  # real request
print(get_weather("London"))  # served from cache
