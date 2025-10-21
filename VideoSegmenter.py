import subprocess
import os

# =============================================
# 🎬 Video Cutter & Merger (FFmpeg + Python)
# Autor: Vinícius Werneck
# Descrição: Corta trechos específicos de um vídeo
#            e junta todos em um único arquivo final.
# =============================================


def tempo_para_segundos(tempo_str):
    """
    Converte tempo no formato MM:SS para segundos (float)
    Exemplo: "3:45" → 225.0
    """
    try:
        minutos, segundos = tempo_str.split(":")
        return int(minutos) * 60 + float(segundos)
    except ValueError:
        raise ValueError("Formato inválido. Use MM:SS (ex: 1:30 para 1 min e 30 seg).")


def obter_intervalos_teclado():
    """
    Permite ao usuário digitar os intervalos manualmente (formato MM:SS).
    Retorna uma lista de tuplas (inicio, fim) em segundos.
    """
    intervalos = []

    print("\n🎬 Modo interativo de corte")
    print("Digite o tempo inicial e final no formato MM:SS (ex: 0:15 a 1:30)")
    print("Pressione ENTER em branco para encerrar.\n")

    while True:
        inicio_str = input("⏱️  Início do corte (MM:SS): ").strip()
        if inicio_str == "":
            break

        fim_str = input("⏱️  Fim do corte (MM:SS): ").strip()
        if fim_str == "":
            break

        try:
            inicio = tempo_para_segundos(inicio_str)
            fim = tempo_para_segundos(fim_str)

            if fim <= inicio:
                print("⚠️  O tempo final deve ser maior que o inicial.\n")
                continue

            intervalos.append((inicio, fim))
            print(f"✅ Intervalo adicionado: {inicio_str} → {fim_str}\n")

        except ValueError as e:
            print(f"❌ Erro: {e}\n")
            continue

    return intervalos


def cortar_video_ffmpeg(input_path, intervalos, output_path):
    """
    Corta e junta trechos de vídeo usando FFmpeg
    """
    if not os.path.exists(input_path):
        print(f"❌ Arquivo não encontrado: {input_path}")
        return False

    temp_files = []

    try:
        print("\n🚀 Iniciando processo de corte...")
        print(f"📂 Arquivo de entrada: {input_path}\n")

        # 1️⃣ Cria cortes temporários
        for i, (start, end) in enumerate(intervalos):
            temp_file = f"temp_corte_{i}.mp4"
            temp_files.append(temp_file)

            print(f"✂️  Criando corte {i+1}: {start:.2f}s → {end:.2f}s")

            cmd_cortar = [
                'ffmpeg',
                '-i', input_path,
                '-ss', str(start),
                '-to', str(end),
                '-c', 'copy',
                '-y',
                temp_file
            ]

            result = subprocess.run(cmd_cortar, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"❌ Erro ao cortar trecho {i+1}: {result.stderr}")
                return False

            print(f"✅ Corte {i+1} criado: {temp_file}\n")

        # 2️⃣ Cria lista para concatenação
        lista_arquivos = "lista_concat.txt"
        with open(lista_arquivos, 'w', encoding='utf-8') as f:
            for file in temp_files:
                f.write(f"file '{file}'\n")

        print("🔗 Concatenando todos os cortes...\n")

        cmd_concatenar = [
            'ffmpeg',
            '-f', 'concat',
            '-safe', '0',
            '-i', lista_arquivos,
            '-c', 'copy',
            '-y',
            output_path
        ]

        result = subprocess.run(cmd_concatenar, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"❌ Erro na concatenação: {result.stderr}")
            return False

        print(f"🎉 Vídeo final criado com sucesso: {output_path}\n")
        return True

    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False

    finally:
        # 3️⃣ Limpeza
        print("🧹 Limpando arquivos temporários...")
        for temp_file in temp_files:
            if os.path.exists(temp_file):
                os.remove(temp_file)

        if os.path.exists("lista_concat.txt"):
            os.remove("lista_concat.txt")

        print("✅ Limpeza concluída.\n")


# =============================================
# 🔧 CONFIGURAÇÕES
# =============================================

video_path = r"I:\Projetos\Baixar_videos\Resultados\video2.mp4"
output_path = "video_cortado.mp4"

print("\n🎥 Cortador de Vídeos Interativo (MM:SS)\n")

# Solicita intervalos do usuário
intervalos = obter_intervalos_teclado()

if not intervalos:
    print("❌ Nenhum intervalo informado. Encerrando...\n")
    exit()

# =============================================
# ▶️ EXECUÇÃO
# =============================================

if cortar_video_ffmpeg(video_path, intervalos, output_path):
    print("✅ Processo concluído com sucesso!")
    print(f"📁 Arquivo final: {output_path}")
    print(f"⏱️  Total de cortes: {len(intervalos)}\n")
else:
    print("❌ Falha no processo.\n")
