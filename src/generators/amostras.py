# Gerador de Amostra

from datetime import datetime, timedelta
from config.settings import JSONS_DIR
from src.database.models import Amostra
import random
import json


# --- Carregadores ---

def carregar_materiais():
    with open(JSONS_DIR / 'materiais.json', encoding='utf-8') as f:
        return json.load(f) 


# --- Geradores de valores individuais ---

def gerar_data_recepcao_amostra():
    return datetime.now() - timedelta(days=random.randint(1, 365))

def gerar_codigo_amostra():
    return f"AM-{random.randint(100, 999)}-{random.randint(1000, 9999)}"

def escolher_tipo_material_amostra():
    return random.choice(carregar_materiais())

def escolher_prioridade_amostra():
    return random.choice(["Alta", "Média", "Baixa"])

def escolher_status_amostra():
    return random.choices(
        population = ["Pendente", "Em análise", "Concluído"],
        weights=[0.1, 0.3, 0.6]
    )[0]


# --- Gerador Principal ---

def gerar_amostra(cliente_id: int) -> Amostra:
    return Amostra(
        codigo         = gerar_codigo_amostra(),
        cliente_id     = cliente_id,
        data_recepcao  = gerar_data_recepcao_amostra(),
        tipo_material  = escolher_tipo_material_amostra(),
        prioridade     = escolher_prioridade_amostra(),
        status         = escolher_status_amostra()
    )