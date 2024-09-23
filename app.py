import os
import shutil

def organizar_arquivos(diretorio):
    # Dicionário para armazenar as extensões e suas respectivas pastas
    extensoes = {
        'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documentos': ['.pdf', '.docx', '.txt', '.xlsx'],
        'Vídeos': ['.mp4', '.mov', '.avi'],
        'Áudio': ['.mp3', '.wav'],
        'Outros': []  # Para arquivos sem categoria específica
    }

    # Muda o diretório atual para o que foi passado
    os.chdir(diretorio)

    # Loop através dos arquivos no diretório
    for arquivo in os.listdir():
        # Ignora pastas
        if os.path.isfile(arquivo):
            # Obtém a extensão do arquivo
            _, extensao = os.path.splitext(arquivo)
            movido = False
            
            # Verifica em qual pasta mover o arquivo com base na extensão
            for pasta, tipos in extensoes.items():
                if extensao.lower() in tipos:
                    # Cria a pasta se não existir
                    if not os.path.exists(pasta):
                        os.makedirs(pasta)
                    # Move o arquivo para a pasta correspondente
                    shutil.move(arquivo, os.path.join(pasta, arquivo))
                    movido = True
                    break
            
            # Se a extensão não for encontrada, move para 'Outros'
            if not movido:
                if not os.path.exists('Outros'):
                    os.makedirs('Outros')
                shutil.move(arquivo, os.path.join('Outros', arquivo))

# Chame a função passando o diretório onde os arquivos estão
organizar_arquivos(r'C:\Users\danta\Downloads')
