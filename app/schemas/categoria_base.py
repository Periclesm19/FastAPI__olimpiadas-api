from pydantic import BaseModel


class CategoriaBase(BaseModel):
    nome: str
    
    
class CriarCategoria(CategoriaBase):
    pass


class Categoria(CategoriaBase):
    id: int
    
    class config:
        orm_mode = True