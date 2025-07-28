# Gerador de Cliente

import random
from config.settings import JSONS_DIR
from src.database.models import Cliente
import json


# --- Carregadores ---

def carregar_silabas():
    with open(JSONS_DIR / "silabas.json", "r", encoding="utf-8") as f:
        return json.load(f)


# --- Geradores individuais ---

def gerar_nome_cliente(silabas):
    inicio = random.choice(silabas["inicio"])
    meio = random.choice(silabas["meio"])
    fim = random.choice(silabas["fim"])
    return f"{inicio}{meio}{fim}".title()

def gerar_cnpj_cliente(): 
    return f"{random.randint(10,99)}.{random.randint(100,999)}.{random.randint(100,999)}/0001-{random.randint(10,99)}"

def gerar_email_cliente(nome: str):
    return f"contato@{nome.lower().replace(' ', '')}.com.br"


# --- Gerador Principal ---

def gerar_cliente() -> Cliente:
    silabas = carregar_silabas()

    nome  = gerar_nome_cliente(silabas)
    cnpj  = gerar_cnpj_cliente()
    email = gerar_email_cliente(nome)

    return Cliente(
        nome  = nome,
        cnpj  = cnpj,
        email = email
    )