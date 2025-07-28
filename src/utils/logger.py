# Logger implementado com loguru

from pathlib import Path
from loguru import logger as loguru_logger
import sys

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parents[2]

# Diretório para salvar o log
LOG_DIR = BASE_DIR / "output"
LOG_DIR.mkdir(exist_ok=True)

# Caminho completo do arquivo de log
log_path = LOG_DIR / "lims_faker.log"

# Configuração do loguru
loguru_logger.remove()
loguru_logger.add(sys.stderr, level="INFO")  # Log padrão no console
loguru_logger.add(log_path, rotation="1 MB", retention="10 days", level="DEBUG")  # Log em arquivo

# Exporta como 'logger'
logger = loguru_logger
