# Classes principais do projeto

from datetime import datetime
from dataclasses import dataclass
from typing import Optional

@dataclass
class Cliente:
    nome: str
    cnpj: str
    email: str

    def insert(self):
        return (
            self.nome,
            self.cnpj,
            self.email
        )


@dataclass
class Amostra:
    codigo: str
    cliente_id: int
    data_recepcao: datetime
    tipo_material: str
    prioridade: str
    status: str

    def insert(self):
        return (
            self.codigo,
            self.cliente_id,
            self.data_recepcao,
            self.tipo_material,
            self.prioridade,
            self.status,
        )


@dataclass
class Analise:
    amostra_id: int
    tipo_analise: str
    metodologia: str
    resultado: str
    data_conclusao: Optional[datetime] = None

    def insert(self):
        return (
            self.amostra_id,
            self.tipo_analise,
            self.metodologia,
            self.resultado,
            self.data_conclusao,
        )