from typing import List
from sqlalchemy.orm import Session
from app.main.translationFolder.infrastructure.models.translationFolderModel import TranslationFolderModel
from app.main.translationFolder.domain.model.aggregates.translationFolder import TranslationFolder
import json

class TranslationFolderRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, folder: TranslationFolder):
        db_folder = TranslationFolderModel(
            name=folder.name,
            description=folder.description,
            translation_ids=json.dumps(folder.translation_ids)
        )
        self.db.add(db_folder)
        self.db.commit()
        self.db.refresh(db_folder)
        return db_folder.to_entity()

    def get_all(self):
        folders = self.db.query(TranslationFolderModel).all()
        return [f.to_entity() for f in folders]

    def get_by_id(self, folder_id: int):
        folder = self.db.query(TranslationFolderModel).filter_by(id=folder_id).first()
        return folder.to_entity() if folder else None

    def update(self, folder_id: int, name: str, translation_ids: List[int]):
        folder = self.db.query(TranslationFolderModel).filter_by(id=folder_id).first()
        if not folder:
            raise Exception("Folder not found")

        folder.name = name
        folder.translation_ids = json.dumps(translation_ids)

        self.db.commit()
        self.db.refresh(folder)
        return folder.to_entity()

    def delete(self, folder_id: int) -> bool:
        folder = self.db.query(TranslationFolderModel).filter_by(id=folder_id).first()
        if folder:
            self.db.delete(folder)
            self.db.commit()
            return True
        return False