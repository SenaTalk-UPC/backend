from typing import List

class TranslationFolder:
    def __init__(self, id: int, name: str, description: str, translation_ids: List[int]):
        self.id = id
        self.name = name
        self.description = description
        self.translation_ids = translation_ids

    def add_translation(self, translation_id: int):
        if translation_id not in self.translation_ids:
            self.translation_ids.append(translation_id)

    def remove_translation(self, translation_id: int):
        if translation_id in self.translation_ids:
            self.translation_ids.remove(translation_id)

    def update_name(self, new_name: str):
        self.name = new_name

    def update_description(self, new_description: str):
        self.description = new_description
