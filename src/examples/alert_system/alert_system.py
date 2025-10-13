"""
4. Alert System (Moving Average)

Problem:
You want to trigger an alert if the average latency of requests in the last 5 minutes exceeds a threshold.

Use a Queue/Deque to store (timestamp, latency).

Keep removing old entries beyond 5 minutes.

Calculate moving average in O(1) using running sum.
"""
from collections import deque
from datetime import timedelta, datetime


# Alert System

class AlertSystem:
    def __init__(self,window_minutes,threshold):
        self.window = timedelta(minutes=window_minutes)
        self.threshold = threshold
        self.logs = deque()

    def add_log(self,timestamp,line):
        # Add new log
        if line and timestamp:
            self.logs.append((timestamp,line))
        while self.logs and self.logs[0][0] < timestamp - self.window:
            old_log = self.logs.popleft()
            print(f"[CLEANUP] Removed old log: {old_log[1]}")

        # Count errors and failures
        error_count = sum(1 for _, msg in self.logs if "[ERROR]" in msg or "[FAILURE]" in msg)

        # Trigger alert if above threshold
        if error_count >= self.threshold:
            print(f"[ALERT] {error_count} error logs in last {self.window.seconds // 60} min(s)")
    def get_recent(self):
        return list(self.logs)

def parse_logs_file(line:str):
    """
        Example log format:
        '2025-10-03 10:00:01 INFO Request latency=120ms'
        '2025-10-03 10:01:20 ERROR Request failed with 500'
    """
    parts = line.split(" ",2)
    time_str = parts[0]+" "+parts[1]
    time_formate = datetime.strptime(time_str,"%Y-%m-%d %H:%M:%S")
    return time_formate, parts[2]

if __name__ == '__main__':
    alert = AlertSystem(window_minutes=2,threshold=2)

    with open("app.log", 'r') as f:
        for line_ in f:
            line = line_.strip()
            if not line:
                continue
            ts,msg = parse_logs_file(line)
            alert.add_log(ts,msg)
    print("\nRecent logs in window:")
    for ts, msg in alert.get_recent():
        print(f"{ts.strftime('%H:%M:%S')} {msg}")
