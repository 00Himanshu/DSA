from collections import deque
import time

class CircularQueue:
    def __init__(self, capacity, time_window=600):
        self.capacity = capacity
        self.queue = deque(maxlen=capacity)
        self.time_window = time_window
        self.time_counter = 0  # Initialize with the current time

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def enqueue(self):
        current_time = time.time()
        if self.is_full():
            self.dequeue_old_calls(current_time)

       self.queue.append(current_time)

    def dequeue_old_calls(self, current_time):
        while self.queue and current_time - self.queue[0] > self.time_window:
            self.queue.popleft()

    def dequeue(self):
        if self.is_empty():
            return None  # or another sentinel value

        return self.queue.popleft()

    def get_size(self):
        return len(self.queue)

    def simulate_time_passage(self, seconds):
        self.time_counter += seconds


window_size = 600
call_tracker = CircularQueue(capacity=10, time_window=window_size)

# Simulate calls being received over time
for _ in range(4):
    call_tracker.enqueue()  # Simulate a call

# Print the count of calls in the last 600 seconds
print("Calls in the last 600 seconds:", call_tracker.get_size())

# Simulate a passage of 100 seconds
call_tracker.simulate_time_passage(100)

# Dequeue calls older than the time window
call_tracker.dequeue_old_calls(time.time())

# Print the count of calls after dequeuing old calls
print("Calls after dequeuing old calls:", call_tracker.get_size())
