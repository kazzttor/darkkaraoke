Segue o texto sugerido para o arquivo `README.md` que explica o projeto:

---

# DarkKaraoke ????

**DarkKaraoke** é uma ferramenta que cria vídeos de karaokê (playback sem vocais) a partir de músicas locais em formato MP3 ou diretamente do YouTube. O programa realiza separação de instrumentos, alteração de tonalidade, extração automática de legendas sincronizadas com os vocais e geração de vídeos com imagens de fundo de uso livre.

## Funcionalidades
- ?? **Separação de Instrumentos**: Remove vocais utilizando algoritmos como Demucs ou Spleeter.
- ?? **Alteração de Tonalidade**: Ajusta o tom dos instrumentos, mantendo a bateria inalterada.
- ?? **Geração de Legendas**: Extrai legendas sincronizadas com os vocais utilizando Whisper ou Lyrics.ovh.
- ?? **Criação de Vídeos**: Gera vídeos de karaokê em múltiplas resoluções com imagens de fundo baixadas automaticamente.
- ?? **Suporte a YouTube**: Baixa músicas diretamente do YouTube em formato MP3.
- ??? **Imagens de Fundo Livres**: Utiliza a API do Unsplash para adicionar visuais atrativos e licenciados aos vídeos.

## Requisitos
Certifique-se de ter as seguintes bibliotecas instaladas no seu ambiente Python:

```
yt-dlp
librosa
soundfile
pydub
moviepy
numpy
Pillow
pysrt
requests
openai
openai-whisper
demucs
spleeter
```

## Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/kazzttor/darkkaraoke.git
   cd darkkaraoke
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure as credenciais:
   - Renomeie o arquivo `config/openai_credentials_example.json` para `openai_credentials.json`.
   - Insira suas chaves de API do OpenAI e do Unsplash.

## Uso
### 1. Geração Completa
Gere o karaokê diretamente de uma URL ou arquivo local:
```bash
python src/darkkaraoke.py --entrada "<URL ou caminho para o arquivo>" --artista "Nome do Artista" --song "Título da Música" --key_shift <número de semitons> --legenda whisper
```

### 2. Personalização
- Para incluir legendas externas:
  ```bash
  python src/darkkaraoke.py --gerarvideo --entrada "<caminho>" --arqlegenda "<arquivo.srt>" --artista "Nome do Artista" --song "Título da Música" --key_shift <número de semitons>
  ```

- Para ajustar legendas:
  ```bash
  python src/darkkaraoke.py --ajustarlegenda --arqlegenda "<arquivo.srt>" --artista "Nome do Artista" --song "Título da Música"
  ```

### 3. Imagens de Fundo
Baixe imagens de fundo:
```bash
python src/darkkaraoke.py --gerarbackground 10
```

### Resoluções Disponíveis
Os vídeos gerados suportam as seguintes resoluções:
- **Full HD (1920x1080)** (padrão)
- **4K (3840x2160)**
- **480p (854x480)**
- **Vertical (1080x1920)**
- **Old TV (640x480)**

## Contribuição
Contribuições são bem-vindas! Se encontrar problemas ou tiver ideias para melhorar, abra uma issue ou envie um pull request.

## Licença
Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

Se precisar de mais ajustes ou adições, é só avisar!