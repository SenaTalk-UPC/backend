from app.main.recognition.interfaces.rest.resource.recognitionResource import RecognitionResource

class RecognitionCommandFromResourceAssembler:
    @staticmethod
    def to_sequence(resource: RecognitionResource):
        return resource.sequence
