"""
Heavy computations or I/O that you only need once per instance?
Why it's elegant: Run once, reuse forever.
https://docs.python.org/3/library/functools.html
"""

from functools import cached_property

import requests


class WeatherClient:
    def __init__(self, city):
        self.city = city

    @cached_property
    def data(self):
        return requests.get(f"https://wttr.in/{self.city}?format=j1").json()


client = WeatherClient("Bayport, NY, USA")
print(client.data["current_condition"])
