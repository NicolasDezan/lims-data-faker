# Configuração e criação do Banco de Dados

import sqlite3
import datetime
from config.settings import OUTPUT_DIR

sqlite3.register_adapter(datetime.datetime, lambda val: val.isoformat(" "))
sqlite3.register_converter("timestamp", lambda val: datetime.datetime.fromisoformat(val.decode()))

def criar_banco():
    """Cria as tabelas do projeto no banco SQLite"""
    conn = sqlite3.connect(OUTPUT_DIR / "lims_fake.db", detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cnpj TEXT UNIQUE,
        contato_email TEXT,
        ativo BOOLEAN DEFAULT 1
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS amostras (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT UNIQUE,
        cliente_id INTEGER,
        data_recepcao TIMESTAMP,
        tipo_material TEXT NOT NULL,
        prioridade TEXT CHECK(prioridade IN ('Alta', 'Média', 'Baixa')),
        status TEXT CHECK(status IN ('Pendente', 'Em análise', 'Concluído')),
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS analises (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amostra_id INTEGER,
        tipo_analise TEXT NOT NULL,
        metodologia TEXT,
        resultado TEXT,
        data_conclusao TEXT,
        FOREIGN KEY (amostra_id) REFERENCES amostras(id)
    )
    ''')

    limpar_tabelas(cursor, ['clientes', 'amostras', 'analises'])

    return conn


####################################################
##### DELETE DEFs ##################################
####################################################

def limpar_tabelas(cursor, tabelas):
    for tabela in tabelas:
        cursor.execute(f"DELETE FROM {tabela}")


####################################################
##### INSERT DEFs ##################################
####################################################

def insert_cliente(cursor, cliente):
    cursor.execute(
        "INSERT INTO clientes (nome, cnpj, contato_email) VALUES (?, ?, ?)",
        cliente.insert()
    )
    return cursor.lastrowid

def insert_amostra(cursor, amostra):
    cursor.execute(
        """INSERT INTO amostras 
           (codigo, cliente_id, data_recepcao, tipo_material, prioridade, status)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (
            amostra.insert()
        )
    )
    return cursor.lastrowid

def insert_analise(cursor, analise):
    cursor.execute(
        """INSERT INTO analises 
           (amostra_id, tipo_analise, metodologia, resultado, data_conclusao)
           VALUES (?, ?, ?, ?, ?)""",
        (
            analise.insert()
        )
    )
    return cursor.lastrowid


####################################################
##### SELECT DEFs ##################################
####################################################

def get_data(cursor, coluna, from_tabela):
    cursor.execute(f"SELECT {coluna} FROM {from_tabela}")
    return [row[0] for row in cursor.fetchall()]

def get_where_id(cursor, coluna, from_tabela, where_id):
    cursor.execute(
        f"SELECT {coluna} FROM {from_tabela} WHERE id = {where_id}"
    )
    result = cursor.fetchone()
    return result[0] if result else None

