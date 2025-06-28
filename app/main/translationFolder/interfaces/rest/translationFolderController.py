from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.main.config.database import get_db

from app.main.translationFolder.application.internal.commandservices.transaltionFolderCommandServiceImpl import TranslationFolderCommandServiceImpl
from app.main.translationFolder.application.internal.queryservices.translationFolderQueryServiceImpl import TranslationFolderQueryServiceImpl
from app.main.translationFolder.infrastructure.repositories.translationFolderRepository import TranslationFolderRepository

from app.main.translationFolder.interfaces.rest.resource.createTranslationFolderResource import (
    CreateTranslationFolderResource
)
from app.main.translationFolder.interfaces.rest.resource.updateTranslationFolderResource import UpdateTranslationFolderResource
from app.main.translationFolder.interfaces.rest.transform.createTranslationFolderCommandFromResourceAssembler import CreateTranslationFolderCommandFromResourceAssembler
from app.main.translationFolder.interfaces.rest.transform.translationFolderResourceFromEntityAssembler import TranslationFolderResourceFromEntityAssembler
from app.main.iam.infrastructure.security.security import get_current_user

router = APIRouter(tags=["Translation Folder"])

@router.post("", status_code=status.HTTP_201_CREATED)
def create_folder(resource: CreateTranslationFolderResource, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    repo = TranslationFolderRepository(db)
    service = TranslationFolderCommandServiceImpl(repo)
    command = CreateTranslationFolderCommandFromResourceAssembler.to_command(resource)
    entity = service.create_folder(command)
    result = TranslationFolderResourceFromEntityAssembler.from_entity(entity)
    return {
        "message": "Folder created successfully",
        "status": "success",
        "data": result
    }

@router.get("", status_code=status.HTTP_200_OK)
def get_all_folders(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    repo = TranslationFolderRepository(db)
    service = TranslationFolderQueryServiceImpl(repo)
    entities = service.get_all_folders()
    results = [TranslationFolderResourceFromEntityAssembler.from_entity(f) for f in entities]
    return {
        "message": "Folders retrieved successfully",
        "status": "success",
        "data": results
    }

@router.get("/{folder_id}", status_code=status.HTTP_200_OK)
def get_folder_by_id(folder_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    repo = TranslationFolderRepository(db)
    service = TranslationFolderQueryServiceImpl(repo)
    entity = service.get_folder_by_id(folder_id)
    if entity is None:
        raise HTTPException(status_code=404, detail="Folder not found")
    result = TranslationFolderResourceFromEntityAssembler.from_entity(entity)
    return {
        "message": "Folder retrieved successfully",
        "status": "success",
        "data": result
    }

@router.put("/{folder_id}", status_code=status.HTTP_200_OK)
def update_folder(folder_id: int, resource: UpdateTranslationFolderResource, db: Session = Depends(get_db), user: dict = Depends(get_current_user)
):
    repo = TranslationFolderRepository(db)  # ✅ Esto estaba faltando
    service = TranslationFolderCommandServiceImpl(repo)
    command = CreateTranslationFolderCommandFromResourceAssembler.to_update_command(folder_id, resource)
    entity = service.update_folder(folder_id, command)
    result = TranslationFolderResourceFromEntityAssembler.from_entity(entity)
    return {
        "message": "Folder updated successfully",
        "status": "success",
        "data": result,
    }

@router.delete("/{folder_id}", status_code=status.HTTP_200_OK)
def delete_folder(folder_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    repo = TranslationFolderRepository(db)
    service = TranslationFolderCommandServiceImpl(repo)
    success = service.delete_folder(folder_id)
    if not success:
        raise HTTPException(status_code=404, detail="Folder not found")
    return {
        "message": "Folder deleted successfully",
        "status": "success"
    }

@router.get("/user/{user_id}")
def get_folders_by_user(user_id: int, db: Session = Depends(get_db)):
    repo = TranslationFolderRepository(db)
    service = TranslationFolderQueryServiceImpl(repo)
    folders = service.get_folders_by_user_id(user_id)
    resources = [TranslationFolderResourceFromEntityAssembler.from_entity(f) for f in folders]
    return {
        "message": "Folders retrieved successfully",
        "status": "success",
        "data": resources
    }

@router.get("/user/{user_id}/favorite")
def get_favorite_folder_by_user(user_id: int, db: Session = Depends(get_db)):
    repo = TranslationFolderRepository(db)
    service = TranslationFolderQueryServiceImpl(repo)
    folder = service.get_favorite_folder_by_user_id(user_id)
    if folder is None:
        raise HTTPException(status_code=404, detail="Favorite folder not found")
    result = TranslationFolderResourceFromEntityAssembler.from_entity(folder)
    return {
        "message": "Favorite folder retrieved successfully",
        "status": "success",
        "data": result
    }