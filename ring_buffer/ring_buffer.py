class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.current = 0

    def append(self, item):

        if len(self.buffer) != self.capacity:
            self.buffer.append(item)
        else:
            self.buffer[self.current] = item
            self.current = (self.current + 1) % self.capacity

    def get(self):
        return self.buffer
