# Serviço de Geração e Inserção de Dados

import random
from config.settings            import NUM_CLIENTES, NUM_AMOSTRAS
from src.database.crud          import insert_cliente, insert_amostra, get_data, get_where_id, insert_analise
from src.generators.amostras    import gerar_amostra
from src.generators.analises    import gerar_analises_para_amostra
from src.generators.clientes    import gerar_cliente


##### Fluxo Principal ##############################
def gerar_e_inserir_dados(cursor):
    inserir_clientes_gerados(cursor)
    inserir_amostras_geradas(cursor)
    inserir_analises_geradas(cursor)


####################################################
##### CLIENTES #####################################
####################################################

def inserir_clientes_gerados(cursor):
    for _ in range(NUM_CLIENTES):
        insert_cliente(cursor, gerar_cliente())


####################################################
##### AMOSTRAS #####################################
####################################################

def inserir_amostras_geradas(cursor):
    clientes_ids = get_data(cursor, 'id','clientes')

    for _ in range(NUM_AMOSTRAS):
        random_cliente_id = random.choice(clientes_ids)
        amostra = gerar_amostra(random_cliente_id)
        insert_amostra(cursor, amostra)


####################################################
##### ANÁLISES #####################################
####################################################

def inserir_analises_geradas(cursor):
    amostras_ids = get_data(cursor, 'id', 'amostras')
    for amostra_id in amostras_ids:
        # Gerar análises para esta amostra
        analises = gerar_analises_para_amostra(
            amostra_id      = amostra_id,
            tipo_material   = get_where_id(cursor, 'tipo_material', 'amostras', amostra_id),
            status          = get_where_id(cursor, 'status',        'amostras', amostra_id),
            data_recepcao   = get_where_id(cursor, 'data_recepcao', 'amostras', amostra_id)
        )
        for analise in analises:
            insert_analise(cursor, analise)