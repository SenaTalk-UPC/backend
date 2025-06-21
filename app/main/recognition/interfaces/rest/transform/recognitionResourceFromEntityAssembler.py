from app.main.recognition.domain.model.aggregates.recognition import Recognition
from app.main.recognition.application.internal.dtos.recognitionDTO import RecognitionDTO

class RecognitionResourceFromEntityAssembler:
    @staticmethod
    def from_entity(entity: Recognition) -> RecognitionDTO:
        return RecognitionDTO(
            prediction=entity.prediction,
            confidence=entity.confidence
        )
