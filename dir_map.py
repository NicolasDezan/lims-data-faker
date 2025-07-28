# Script secreto para criar mapinha dos arquivos ignorando as IGNORE_FILES

from pathlib import Path

IGNORE_FILES = [
    'output_dir_map.txt', 
    'dir_map.py',
    '__pycache__',
    '.git',
    '__init__.py',
    '.venv',
    '.idea'
]

def generate_directory_map(root_dir='.', output_file='output/output_dir_map.txt', ignore_files=None):
    """
    Gera um mapeamento da estrutura de diretórios no formato de árvore.
    
    Args:
        root_dir (str): Diretório raiz para mapear (padrão: diretório atual)
        output_file (str): Nome do arquivo de saída
        ignore_files (list): Lista de arquivos para ignorar
    """
    if ignore_files is None:
        ignore_files = IGNORE_FILES
    
    root_path = Path(root_dir)
    output_lines = []
    
    def build_tree(path, prefix=''):
        """Função recursiva para construir a árvore de diretórios"""
        contents = sorted([p for p in path.iterdir() if p.name not in ignore_files])
        
        for index, item in enumerate(contents):
            if index == len(contents) - 1:
                new_prefix = prefix + "    "
                line_prefix = "└── "
            else:
                new_prefix = prefix + "│   "
                line_prefix = "├── "
            
            if item.is_dir():
                output_lines.append(f"{prefix}{line_prefix}{item.name}/")
                build_tree(item, new_prefix)
            else:
                # Adiciona comentário para arquivos Python
                comment = "  # " + get_file_comment(item) if item.suffix == '.py' else ""
                output_lines.append(f"{prefix}{line_prefix}{item.name}{comment}")
    
    def get_file_comment(file_path):
        """Extrai a primeira linha de comentário do arquivo como descrição"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                first_line = file.readline().strip()
                if first_line.startswith('#'):
                    return first_line[1:].strip()
        except:
            pass
        return ""
    
    # Inicia a construção da árvore
    output_lines.append(f"{root_path.name}/")
    build_tree(root_path)
    
    # Escreve no arquivo de saída
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(output_lines))
    
    print(f"Mapa de diretórios gerado em: {output_file}")

if __name__ == "__main__":
    generate_directory_map()