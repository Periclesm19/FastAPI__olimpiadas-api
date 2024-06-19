from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.atleta_base import Atleta, CriarAtleta, AtualizarAtleta
from app.database import get_db
from app.crud import atleta_crud


router = APIRouter()


@router.get('/atletas/{atleta_id}', response_model=Atleta, tags=['Atletas',])
def ler_atleta(atleta_id: int, db: Session = Depends(get_db)):
    db_atleta = atleta_crud.get_atleta(db, atleta_id)
    
    if db_atleta is None:
        raise HTTPException(status_code=404, detail= 'Atleta não encontrado.')
    
    return db_atleta


@router.get('/atletas/', response_model=List[Atleta], tags=['Atletas',])
def ler_atletas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    atletas = atleta_crud.get_atletas(db, skip, limit)
    
    return atletas


@router.post('/atletas/', response_model=Atleta, tags= ['Atletas',])
def criar_atleta(atleta: CriarAtleta, db: Session = Depends(get_db)):
    return atleta_crud.create_atleta(db=db, atleta=atleta)


@router.put('/atletas/{atleta_id}', response_model=Atleta, tags=['Atletas',])
def atualizar_atleta(atleta_id: int, atleta: AtualizarAtleta, db: Session = Depends(get_db)):
    db_atleta = atleta_crud.update_atleta(db, atleta_id, atleta)
    
    if db_atleta is None:
        raise HTTPException(status_code=404, detail= 'Atleta não encontrado.')
    
    return db_atleta


@router.delete('/atletas/{atleta_id}', response_model=Atleta, tags=['Atletas',])
def deletar_atleta(atleta_id: int, db: Session = Depends(get_db)):
    db_atleta = atleta_crud.delete_atleta(db, atleta_id)
    
    if db_atleta is None:
        raise HTTPException(status_code=404, detail= 'Atleta não encontrado.')
    
    return db_atleta