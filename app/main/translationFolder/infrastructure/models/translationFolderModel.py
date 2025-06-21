from sqlalchemy import Column, Integer, String
from app.main.config.database import Base
import json

class TranslationFolderModel(Base):
    __tablename__ = "translation_folders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    translation_ids = Column(String)  # Se almacenará como JSON string

    def to_entity(self):
        from app.main.translationFolder.domain.model.aggregates.translationFolder import TranslationFolder
        return TranslationFolder(
            id=self.id,
            name=self.name,
            description=self.description,
            translation_ids=json.loads(self.translation_ids) if self.translation_ids else []
        )
