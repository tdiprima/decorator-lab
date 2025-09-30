# The Tenacity equivalent of the Retry Decorator
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=0.5, min=0.5, max=10)
)
def example_function():
    # Your function implementation here
    pass
