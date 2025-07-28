import sys

from config.settings import VERSAO_PYTHON_REQUIRIDA
from src.utils.logger import logger


def check_python_version():
    """Verifica a versão do Python automaticamente baseado em config.py"""
    try:
        # Extrai major, minor, micro da string (ex: "3.12.10" → (3, 12, 10))
        required_major, required_minor, required_micro = map(int, VERSAO_PYTHON_REQUIRIDA.split('.'))

        current_major, current_minor, current_micro = sys.version_info.major, sys.version_info.minor, sys.version_info.micro

        current_version = f"{current_major}.{current_minor}.{current_micro}"
        required_version = f"{required_major}.{required_minor}.{required_micro}"

        if (current_major, current_minor, current_micro) != (required_major, required_minor, required_micro):


            logger.warning(
                f"️  Aviso: Você está usando Python {current_version} (Recomendado: {required_version})\n"
                "   Algumas funcionalidades podem se comportar diferente.\n"
                "   Considere usar pyenv para instalar a versão exata:\n"
                "   $ pyenv install 3.12.10 && pyenv local 3.12.10"
            )
        else:
            logger.debug(f'Python está rodando na versão: {required_version}')

    except (AttributeError, ValueError) as e:
        logger.error(f"Erro ao verificar versão do Python: {str(e)}")