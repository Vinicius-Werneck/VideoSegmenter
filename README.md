# 🎬 Video Cutter & Merger

Um script Python para cortar trechos específicos de vídeos e juntá-los em um único arquivo final usando FFmpeg.

## 📋 Descrição

Este projeto permite cortar múltiplos trechos de um vídeo baseado em intervalos de tempo fornecidos pelo usuário e combinar todos os cortes em um único arquivo de saída.

## ✨ Funcionalidades

- 🎥 Corte de vídeos usando FFmpeg
- ⏱️ Entrada de tempos no formato MM:SS (minutos:segundos)
- 🔗 Concatenação automática dos cortes
- 🧹 Limpeza automática de arquivos temporários
- 🖥️ Interface interativa via terminal

## 📋 Pré-requisitos

- Python 3.x
- FFmpeg instalado e configurado no PATH do sistema

### Instalando o FFmpeg

**Windows:**
```bash
# Via chocolatey
choco install ffmpeg

# Ou baixe do site oficial: https://ffmpeg.org/download.html
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

**macOS:**
```bash
# Via Homebrew
brew install ffmpeg
```

## 🚀 Como usar

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd video-cutter-merger
```

2. Configure o caminho do vídeo de entrada no script:
```python
video_path = r"caminho/para/seu/video.mp4"
```

3. Execute o script:
```bash
python video_cutter.py
```

4. Siga as instruções interativas:
   - Digite os tempos iniciais e finais no formato `MM:SS`
   - Pressione ENTER em branco para finalizar a entrada
   - O script processará os cortes e gerará o vídeo final

## 📝 Exemplo de uso

```
🎥 Cortador de Vídeos Interativo (MM:SS)

🎬 Modo interativo de corte
Digite o tempo inicial e final no formato MM:SS (ex: 0:15 a 1:30)
Pressione ENTER em branco para encerrar.

⏱️  Início do corte (MM:SS): 0:15
⏱️  Fim do corte (MM:SS): 0:30
✅ Intervalo adicionado: 0:15 → 0:30

⏱️  Início do corte (MM:SS): 1:45
⏱️  Fim do corte (MM:SS): 2:15
✅ Intervalo adicionado: 1:45 → 2:15

⏱️  Início do corte (MM:SS): [ENTER]

🚀 Iniciando processo de corte...
```

## 🛠️ Estrutura do projeto

```
video-cutter-merger/
├── video_cutter.py    # Script principal
├── README.md          # Este arquivo
└── requirements.txt   # Dependências (se houver)
```

## 📄 Licença

Este projeto é de uso livre.

## 👨‍💻 Autor

Vinícius Werneck

## ⚠️ Observações

- Certifique-se de que o FFmpeg está instalado e acessível pelo sistema
- O script cria arquivos temporários que são automaticamente removidos ao final do processo
- Funciona melhor com arquivos MP4
- Mantenha backups dos seus vídeos originais

---

**Happy coding!** 🎬✨