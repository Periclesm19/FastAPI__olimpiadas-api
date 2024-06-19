from sqlalchemy.orm import Session
from app.models.atleta import Atleta as DBAtleta
from app.schemas.atleta_base import AtualizarAtleta, CriarAtleta


def get_atleta(db: Session, atleta_id: int):
    return db.query(DBAtleta).filter(DBAtleta.id == atleta_id).first()


def get_atletas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(DBAtleta).offset(skip).limit(limit).all()


def create_atleta(db: Session, atleta: CriarAtleta):
    db_atleta = DBAtleta(**atleta.model_dump())
    db.add(db_atleta)
    db.commit()
    db.refresh(db_atleta)
    
    return db_atleta


def update_atleta(db: Session, atleta_id: int, atleta: AtualizarAtleta):
    db_atleta = db.query(DBAtleta).filter(DBAtleta.id == atleta_id).first()
    
    if db_atleta:
        for cahve, valor in atleta.model_dump().items():
            setattr(db_atleta, cahve, valor)
        
        db.add(db_atleta)    
        db.commit()
        db.refresh(db_atleta)
    
    return db_atleta


def delete_atleta(db: Session, atleta_id: int):
    db_atleta = db.query(DBAtleta).filter(DBAtleta.id == atleta_id).first()
    
    if db_atleta:
        db.delete(db_atleta)
        db.commit()
        
    return db_atleta
            
