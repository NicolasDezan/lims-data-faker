# Gerador de Análises

import random
import json
from datetime import datetime, timedelta
from typing import Dict, Any
from config.settings import JSONS_DIR
from src.database.models import Analise


# --- Carregadores ---

def carregar_config_analises() -> Dict[str, Any]:
    with open(JSONS_DIR / "analises.json", "r", encoding="utf-8") as f:
        return json.load(f)


# --- Geradores de valores individuais ---

def escolher_tipo_analise(tipo_material: str, config: dict) -> str:
    if "Água" in tipo_material:
        return random.choice(["Microbiologia", "Físico-Química"])
    elif "Solo" in tipo_material:
        return random.choice(["Metais Pesados", "Físico-Química"])
    else:
        return random.choice(list(config.keys()))

def escolher_metodologia_analise(tipo_analise: str, config: dict) -> str:
    return random.choice(config[tipo_analise]["metodologias"])

def gerar_resultado_analise(tipo_analise: str, config: dict) -> str:
    return random.choice(config[tipo_analise]["resultados"])

def gerar_data_conclusao_analise(prioridade: str, data_recepcao: datetime) -> datetime:
    if prioridade == "Alta":
        dias = random.randint(1, 3)
    elif prioridade == "Média":
        dias = random.randint(4, 15)
    else:  # Baixa
        dias = random.randint(16, 60)
    return data_recepcao + timedelta(days=dias)


# --- Geradores Principais ---

def gerar_analises_para_amostra(amostra_id: int,
                                tipo_material: str,
                                status: str,
                                data_recepcao: datetime,
                                num_analises: int = 3) -> list[Analise]:
    return [
        gerar_analise(amostra_id, tipo_material, status, data_recepcao)
        for _ in range(num_analises)
    ]


def gerar_analise(amostra_id: int,
                  tipo_material: str,
                  status: str,
                  data_recepcao: datetime) -> Analise:
    config = carregar_config_analises()

    tipo = escolher_tipo_analise(tipo_material, config)
    metodologia = escolher_metodologia_analise(tipo, config)
    resultado = gerar_resultado_analise(tipo, config) if status == "Concluído" else None
    data_conclusao = gerar_data_conclusao_analise(status, data_recepcao) if status == "Concluído" else None

    return Analise(
        amostra_id      = amostra_id,
        tipo_analise    = tipo,
        metodologia     = metodologia,
        resultado       = resultado,
        data_conclusao  = data_conclusao
    )
