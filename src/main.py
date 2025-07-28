# Ponto de Entrada

from config.settings import NUM_CLIENTES, NUM_AMOSTRAS, NUM_ANALISES_POR_AMOSTRA
from src.database.crud import criar_banco
from src.services.db.insert_generations import gerar_e_inserir_dados
from src.utils.logger import logger
from src.utils.sys_checks import check_python_version


def main():
    check_python_version()

    logger.info("Iniciando a geração de dados LIMS...")
    logger.debug(f"Configurações: {NUM_CLIENTES=} {NUM_AMOSTRAS=} {NUM_ANALISES_POR_AMOSTRA=}")

    conn = criar_banco()
    cursor = conn.cursor()

    try:
        gerar_e_inserir_dados(cursor)
        logger.success("Dados gerados com sucesso!")
    except Exception as e:
        logger.exception(f"Erro durante a geração de dados: {e}")

    try:
        conn.commit()
        conn.close()
        logger.debug("Conexão com o banco de dados encerrada")
    except Exception as e:
        logger.exception(f"Erro durante a desconexão com o banco de dados: {e}")
    finally:
        logger.info("Programa encerrado")


if __name__ == "__main__":
    main()