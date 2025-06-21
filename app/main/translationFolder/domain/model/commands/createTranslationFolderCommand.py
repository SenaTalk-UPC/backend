class CreateTranslationFolderCommand:
    def __init__(self, name: str, description: str, translation_ids: list[int]):
        self.name = name
        self.description = description
        self.translation_ids = translation_ids
