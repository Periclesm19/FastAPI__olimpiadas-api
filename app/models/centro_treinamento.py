from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class CentroTreinamento(Base):
    __tablename__ = 'centros_treinamento'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    endereco = Column(String, unique=True, index=True)
    proprietario = Column(String, index=True)