import re

class Email:
    def __init__(self, address: str):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", address):
            raise ValueError("Email inválido")
        self.address = address
