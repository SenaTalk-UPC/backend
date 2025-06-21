from datetime import datetime

class Translation:
    def __init__(self, user_email: str, text: str, created_at: datetime = None):
        self.user_email = user_email
        self.text = text
        self.created_at = created_at or datetime.utcnow()
