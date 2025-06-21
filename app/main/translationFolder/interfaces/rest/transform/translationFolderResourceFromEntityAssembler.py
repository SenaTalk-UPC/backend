from app.main.translationFolder.domain.model.aggregates.translationFolder import TranslationFolder
from app.main.translationFolder.interfaces.rest.resource.translationFolderResource import TranslationFolderResource

class TranslationFolderResourceFromEntityAssembler:

    @staticmethod
    def from_entity(entity: TranslationFolder) -> TranslationFolderResource:
        return TranslationFolderResource(
            id=entity.id,
            name=entity.name,
            description=entity.description,
            translation_ids=entity.translation_ids
        )
