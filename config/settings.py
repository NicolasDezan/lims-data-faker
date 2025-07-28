# Configurações do projeto

from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent.parent
JSONS_DIR = BASE_DIR / "config" / "jsons"
OUTPUT_DIR = BASE_DIR / "output"

# Configurações
NUM_CLIENTES = 20
NUM_AMOSTRAS = 100
NUM_ANALISES_POR_AMOSTRA = 3

# Python
VERSAO_PYTHON_REQUIRIDA = "3.12.10"