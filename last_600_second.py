class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [0] * capacity
        self.front = self.rear = -1
        self.size = 0
        self.time_counter = 0 

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self):
        if self.is_full():

            self.dequeue()

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = self.time_counter
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None

        item = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        self.size -= 1

        return item

    def get_size(self):
        return self.size

    def simulate_time_passage(self, seconds):
        self.time_counter += seconds

# Example usage:
window_size = 600
call_tracker = CircularQueue(window_size)

# Simulate calls being received over time
for _ in range(1):
    call_tracker.enqueue()  # Simulate a call
    print("Calls in the last 600 seconds:", call_tracker.get_size())
    call_tracker.simulate_time_passage(3)# Simulate a passage of 100 seconds