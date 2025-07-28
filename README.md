# LIMS DATA FAKER

Gerador de dados sintéticos para simular registros de um sistema LIMS (Laboratory Information Management System). Visa o estudo de SQLite aplicado a dados laboratoriais.

---

## Funcionalidades

- Gera clientes com nomes fictícios
- Gera amostras com atributos como status, tipo de material e data
- Gera análises laboratoriais baseadas nas amostras e materiais
- Permite configuração do volume de dados gerados
- Salva os dados em um banco SQLite pronto para uso e consulta


---

## Estrutura do Projeto


```
lims-data-faker/
├── config/
│   ├── jsons/                          # Arquivos de apoio para a geração de dados
│   └── settings.py                     # Configurações gerais do projeto
├── src/
│   ├── database/
│   │   ├── crud.py                     # Funções de interação direta com o banco (inserção, query, limpeza)
│   │   └── models.py                   # Definição das classes principais (entidades)
│   ├── generators/                     # Geração de dados sintéticos para cada entidade
│   │   ├── amostras.py
│   │   ├── analises.py
│   │   └── clientes.py
│   ├── services/
│   │   └── db/
│   │       └── insert_generations.py   # Orquestração de inserções no banco
│   └── utils/
│   │   └── logger.py                   # Logger implementado com loguru
│   └── main.py                         # Ponto de entrada principal
```

---

## Configurações

As configurações de execução estão em `config/settings.py`:

```python
NUM_CLIENTES = 20
NUM_AMOSTRAS = 100
NUM_ANALISES_POR_AMOSTRA = 3
```

Você pode alterar esses valores para gerar mais ou menos dados.


---

## Como Usar

### Pré-requisito

- Python 3.12.10 *(versão no desenvolvimento/outras versões **podem** ser compatíveis)*


### 1. Clone o repositório

```bash
git clone https://github.com/NicolasDezan/lims-data-faker.git
cd lims-data-faker
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Execute o gerador

```bash
python -m src.main
```

> Isso criará um banco SQLite com dados gerados aleatoriamente no diretório `output/`.

---

Feito por Nícolas Dezan dos Santos.
