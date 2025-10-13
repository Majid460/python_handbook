"""
Problem:
You need to design a rate limiter for an API. A user can make at most N requests per second. If more requests come, they must be rejected and logged.

Use Queue/Deque to store timestamps of requests.

When a new request comes in, check if the oldest request in the queue is outside the 1-second window.

Log rejected requests.

Example Log Output:
[INFO] User123 request accepted at 10:00:01.001
[INFO] User123 request accepted at 10:00:01.200
[WARN] User123 request throttled at 10:00:01.300
"""
import logging
import threading
import time
from collections import deque
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class RequestLog:
    user: str = None
    status: str = None
    time_stamp: float = field(default_factory=time.time)

    def log_message(self):
        # Convert timestamp to formatted string
        formatted_time = datetime.fromtimestamp(self.time_stamp).strftime("%H:%M:%S.%f")[:-3]  # milliseconds
        print(f"[{self.status}] {self.user} request at {formatted_time}")
# Configure Logging
# logging.basicConfig(
#     level = logging.INFO,
#     format= '[%(levelname)s] %(message)s at %(asctime)s',
#     datefmt= '%H:%M:%S.%f'
# )


class RateLimiter:

    def __init__(self, req_limit):
        """
        :param req_limit: Requests per second allowed
        """
        self.requests = {}
        self.req_limit = req_limit

    # store timestamps of each request
    def get_req(self, request: RequestLog):
        now = request.time_stamp
        user_queue = self.requests.get(request.user, deque())

        # Remove timestamps older than 1 second
        while user_queue and now - user_queue[0] >= 1:
            user_queue.popleft()

        if len(user_queue) < self.req_limit:
            # Accept request
            request.status = "INFO"
            user_queue.append(now)
        else:
            # Reject request
            request.status = "WARN"

        self.requests[request.user] = user_queue
        request.log_message()


    def start(self):
        while True:
            # Simulate 3 requests at once
            requests = [RequestLog("User123") for _ in range(3)]
            for r in requests:
                self.get_req(r)
            time.sleep(0.5)

if __name__ == '__main__':
    rate_limiter = RateLimiter(2)
    # do on thread

    t1 = threading.Thread(target= rate_limiter.start(), daemon= True)
    t1.start()
    # Keep main thread alive
    while True:
        time.sleep(1)

