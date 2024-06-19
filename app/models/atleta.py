from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base


class Atleta(Base):
    __tablename__ = 'atletas'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    idade = Column(Integer, index=True)
    peso = Column(Float, index=True)
    altura = Column(Float, index=True)