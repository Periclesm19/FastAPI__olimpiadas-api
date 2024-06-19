from pydantic import BaseModel


class AtletaBase(BaseModel):
    nome: str
    idade: int
    peso: float
    altura: float
    
    
class CriarAtleta(AtletaBase):
    pass


class AtualizarAtleta(AtletaBase):
    pass


class Atleta(AtletaBase):
    id: int
    
    class config:
        orm_mode = True 