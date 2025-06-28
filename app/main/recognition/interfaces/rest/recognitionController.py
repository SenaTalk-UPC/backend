# app/main/recognition/interfaces/rest/recognitionController.py
from fastapi import APIRouter
from app.main.recognition.application.internal.dtos.recognitionDTO import RecognitionRequest, RecognitionResponse
from app.main.recognition.application.internal.queryservices.recognitionQueryServiceImpl import RecognitionQueryServiceImpl

router = APIRouter(tags=["Recognition"])

@router.post("")
def recognize(request: RecognitionRequest):
    service = RecognitionQueryServiceImpl()
    result = service.predict(request.keypoints)
    return {"result": result}
