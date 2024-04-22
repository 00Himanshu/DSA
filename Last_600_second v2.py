from collections import deque
import time

class CallTracker:
    def __init__(self, window_size=600):
        self.calls = deque(maxlen=window_size)  # Using a deque with a maximum length to act as a sliding window

    def receive_call(self):
        timestamp = time.time()  # Use the current time as a timestamp for the call
        self.calls.append(timestamp)

    def get_calls_in_last_600_seconds(self):
        current_time = time.time()
        # Filter calls within the last 600 seconds
        recent_calls = [call for call in self.calls if current_time - call <= 600]
        return len(recent_calls)


call_tracker = CallTracker()

# Simulate receiving some calls
call_tracker.receive_call()
call_tracker.receive_call()
call_tracker.receive_call()
call_tracker.receive_call()

print("Calls in the last 600 seconds:", call_tracker.get_calls_in_last_600_seconds())
