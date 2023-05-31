from pydantic import BaseModel

class DadosLembrete(BaseModel):
    id: str
    texto: str
    sentimento: str