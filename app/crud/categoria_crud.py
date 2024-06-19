from sqlalchemy.orm import Session
from app.models.categoria import Categoria as DBCategoria
from app.schemas.categoria_base import CriarCategoria



def get_categoria(db: Session, categoria_id: int):
    return db.query(DBCategoria).filter(DBCategoria.id == categoria_id).first()


def get_categorias(db: Session, skip: int = 0, limit: int = 10):
    return db.query(DBCategoria).offset(skip).limit(limit).all()


def create_categoria(db: Session, categoria: CriarCategoria):
    db_categoria = DBCategoria(
        nome = categoria.nome
    )
    
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    
    return db_categoria