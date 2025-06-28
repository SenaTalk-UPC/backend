from datetime import datetime

class Translation:
    def __init__(self, text: str, folder_id: int, created_at: datetime = None):
        self.text = text
        self.folder_id = folder_id
        self.created_at = created_at or datetime.utcnow()
