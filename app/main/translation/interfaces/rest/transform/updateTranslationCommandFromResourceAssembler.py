from app.main.translation.interfaces.rest.resources.updateTranslationResource import UpdateTranslationResource

class UpdateTranslationCommandFromResourceAssembler:
    @staticmethod
    def to_dict(resource: UpdateTranslationResource) -> dict:
        return {"text": resource.text}
