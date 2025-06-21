from typing import List

class Vector:
    def __init__(self, data: List[List[float]]):
        if len(data) != 30 or any(len(row) != 243 for row in data):
            raise ValueError("Vector must be of shape (30, 243)")
        self.data = data
