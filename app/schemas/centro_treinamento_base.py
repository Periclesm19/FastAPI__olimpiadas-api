from pydantic import BaseModel


class CentroTreinamentoBase(BaseModel):
    nome: str
    endereco: str
    proprietario: str
    
    
class CriarCentroTreinamento(CentroTreinamentoBase):
    pass


class CentroTreinamento(CentroTreinamentoBase):
    id: int
    
    class config:
        orm_mode = True