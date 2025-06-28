from sqlalchemy import Column, Integer, String
from app.main.config.database import Base
import json
from app.main.translationFolder.domain.model.aggregates.translationFolder import TranslationFolder


class TranslationFolderModel(Base):
    __tablename__ = "translation_folders"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    userId = Column(Integer, nullable=False)

    def to_entity(self):
        return TranslationFolder(
            id=self.id,
            name=self.name,
            description=self.description,
            userId=self.userId
        )
