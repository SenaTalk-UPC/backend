from app.main.recognition.domain.model.aggregates.recognition import Recognition
from app.main.recognition.interfaces.rest.resource.recognitionResource import RecognitionResponseResource

class RecognitionResourceFromEntityAssembler:
    @staticmethod
    def from_entity(entity: Recognition) -> RecognitionResponseResource:
        return RecognitionResponseResource(text=entity.text, confidence=entity.confidence)
