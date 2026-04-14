# You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

# Max heap for the processing of tasks
# Queue for the cooldown period of the tasks
from collections import deque
import heapq
from typing import Counter, List


class TaskScheduler:
    def leastinterval(self, tasks: List[str], n: int) -> int:
        # To convert into dict type with length -> A:2
        count = Counter(tasks)
        # init a max heap
        max_heap = [
            -c for c in count.values()
        ]  # I will only keep heap of counts not keys
        heapq.heapify(max_heap)
        queue = (
            deque()
        )  # (remaining count,idle time ) time -> after how much this value will be available
        time = 0
        # loop while heap or queue
        while queue or max_heap:
            time += 1
            if max_heap:
                # e.g. heap -> -3,-2
                cnt = 1 + heapq.heappop(
                    max_heap
                )  # cnt -> count  # +1 to reduce the one value of count
                # if count not zero
                if cnt:
                    # append it in queue
                    # count , time for next availability + current time
                    queue.append((cnt, time + n))

            if (
                queue and queue[0][1] == time
            ):  # [0] -> means first element , [1] -> second element in the pair
                # so we need to push the count into the heap
                heapq.heappush(max_heap, queue.popleft()[0])
        return time


if __name__ == "__main__":
    task_scheduler = TaskScheduler()
    tasks: List[str] = ["A", "A", "A", "B", "C"]
    n = 3
    print(task_scheduler.leastinterval(tasks, n))
