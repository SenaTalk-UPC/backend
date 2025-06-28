# app/main/translationFolder/domain/model/commands/updateTranslationCommand.py

from typing import List, Optional

class UpdateTranslationFolderCommand:
    def __init__(self, folder_id: int, name: Optional[str] = None, description: Optional[str] = None, userId: Optional[int] = None):
        self.folder_id = folder_id
        self.name = name
        self.description = description
        self.userId = userId
