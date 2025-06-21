class User:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password  # en producción esto debe ser un hash
