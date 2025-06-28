import numpy as np
from collections import deque

class FrameBuffer:
    def __init__(self, max_length: int = 30):
        self.buffer = deque(maxlen=max_length)
        self.max_length = max_length

    def add_frame(self, frame_vector: np.ndarray):
        self.buffer.append(frame_vector)

    def is_full(self):
        return len(self.buffer) == self.max_length

    def get_sequence(self):
        if not self.is_full():
            raise ValueError("Buffer is not full yet")
        return np.stack(self.buffer, axis=0)  # Shape: (30, 1662)

    def reset(self):
        self.buffer.clear()
