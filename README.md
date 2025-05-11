# 📂 Organizador de Arquivos
Um script Python simples para organizar automaticamente arquivos em pastas baseadas em suas extensões.

# 📋 Visão Geral
Este script ajuda a organizar arquivos em um diretório específico, movendo-os para pastas categorizadas por tipo (Imagens, Documentos, Vídeos, etc.). Arquivos com extensões não especificadas são movidos para uma pasta "Outros".

# 🛠 Funcionalidades
Organiza arquivos por tipo/extensão
Cria automaticamente pastas de categorias quando necessário
Lida com extensões de arquivo em maiúsculas/minúsculas
Move arquivos não categorizados para a pasta "Outros"

# 📂 Categorias de Arquivos
Pasta	Extensões Suportadas
Imagens	.jpg, .jpeg, .png, .gif
Documentos	.pdf, .docx, .txt, .xlsx
Vídeos	.mp4, .mov, .avi
Áudio	.mp3, .wav
Outros	Qualquer extensão não listada acima

# ⚙️ Como Usar
Pré-requisitos:
Python 3.x instalado
Permissões de leitura/escrita no diretório alvo

# Instalação:
bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

# Execução:
Modifique o caminho do diretório na última linha do script para o caminho que deseja organizar

# Execute o script:
bash
python organizador_arquivos.py

# Personalização:
Para adicionar mais categorias ou extensões, edite o dicionário extensoes no script

#📝 Exemplo de Uso
python
# Para organizar sua pasta Downloads:
organizar_arquivos(r'C:\Users\danta\Downloads')

# Para organizar outra pasta:
organizar_arquivos(r'C:\Users\danta\Desktop\PastaDesorganizada')

# ⚠️ Limitações
Não lida com arquivos com nomes duplicados
Não organiza subpastas (apenas arquivos no diretório raiz)
Movimentação é permanente (não há "undo")
