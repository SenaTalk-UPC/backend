from fastapi import APIRouter, Depends
from app.main.recognition.interfaces.rest.resource.recognitionResource import RecognitionRequestResource
from app.main.recognition.interfaces.rest.transform.recognitionResourceFromEntityAssembler import RecognitionResourceFromEntityAssembler
from app.main.recognition.application.internal.queryservices.recognitionQueryServiceImpl import RecognitionQueryServiceImpl

router = APIRouter(tags=["Recognition"])

service = RecognitionQueryServiceImpl()

@router.post("")
def recognize(request: RecognitionRequestResource):
    result = service.predict(request.keypoints)
    response = RecognitionResourceFromEntityAssembler.from_entity(result)
    return {
        "status": "success",
        "data": response
    }
