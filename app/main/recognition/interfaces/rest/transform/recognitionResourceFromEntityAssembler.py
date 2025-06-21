from app.main.recognition.domain.model.aggregates.recognition import Recognition

class RecognitionResourceFromEntityAssembler:
    @staticmethod
    def from_entity(entity: Recognition) -> dict:
        return {
            "recognized_word": entity.recognized_word,
            "confidence": entity.confidence
        }
