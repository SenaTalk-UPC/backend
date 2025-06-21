from app.main.translation.infrastructure.models.translationModel import TranslationModel
from app.main.translation.interfaces.rest.resources.translationResource import TranslationResource

class TranslationResourceFromEntityAssembler:
    @staticmethod
    def from_entity(entity: TranslationModel) -> TranslationResource:
        return TranslationResource(
            id=entity.id,
            user_email=entity.user_email,
            text=entity.text
        )
