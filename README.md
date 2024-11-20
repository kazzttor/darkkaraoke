Segue o texto sugerido para o arquivo `README.md` que explica o projeto:

---

# DarkKaraoke ????

**DarkKaraoke** � uma ferramenta que cria v�deos de karaok� (playback sem vocais) a partir de m�sicas locais em formato MP3 ou diretamente do YouTube. O programa realiza separa��o de instrumentos, altera��o de tonalidade, extra��o autom�tica de legendas sincronizadas com os vocais e gera��o de v�deos com imagens de fundo de uso livre.

## Funcionalidades
- ?? **Separa��o de Instrumentos**: Remove vocais utilizando algoritmos como Demucs ou Spleeter.
- ?? **Altera��o de Tonalidade**: Ajusta o tom dos instrumentos, mantendo a bateria inalterada.
- ?? **Gera��o de Legendas**: Extrai legendas sincronizadas com os vocais utilizando Whisper ou Lyrics.ovh.
- ?? **Cria��o de V�deos**: Gera v�deos de karaok� em m�ltiplas resolu��es com imagens de fundo baixadas automaticamente.
- ?? **Suporte a YouTube**: Baixa m�sicas diretamente do YouTube em formato MP3.
- ??? **Imagens de Fundo Livres**: Utiliza a API do Unsplash para adicionar visuais atrativos e licenciados aos v�deos.

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

## Instala��o
1. Clone o reposit�rio:
   ```bash
   git clone https://github.com/kazzttor/darkkaraoke.git
   cd darkkaraoke
   ```

2. Instale as depend�ncias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure as credenciais:
   - Renomeie o arquivo `config/openai_credentials_example.json` para `openai_credentials.json`.
   - Insira suas chaves de API do OpenAI e do Unsplash.

## Uso
### 1. Gera��o Completa
Gere o karaok� diretamente de uma URL ou arquivo local:
```bash
python src/darkkaraoke.py --entrada "<URL ou caminho para o arquivo>" --artista "Nome do Artista" --song "T�tulo da M�sica" --key_shift <n�mero de semitons> --legenda whisper
```

### 2. Personaliza��o
- Para incluir legendas externas:
  ```bash
  python src/darkkaraoke.py --gerarvideo --entrada "<caminho>" --arqlegenda "<arquivo.srt>" --artista "Nome do Artista" --song "T�tulo da M�sica" --key_shift <n�mero de semitons>
  ```

- Para ajustar legendas:
  ```bash
  python src/darkkaraoke.py --ajustarlegenda --arqlegenda "<arquivo.srt>" --artista "Nome do Artista" --song "T�tulo da M�sica"
  ```

### 3. Imagens de Fundo
Baixe imagens de fundo:
```bash
python src/darkkaraoke.py --gerarbackground 10
```

### Resolu��es Dispon�veis
Os v�deos gerados suportam as seguintes resolu��es:
- **Full HD (1920x1080)** (padr�o)
- **4K (3840x2160)**
- **480p (854x480)**
- **Vertical (1080x1920)**
- **Old TV (640x480)**

## Contribui��o
Contribui��es s�o bem-vindas! Se encontrar problemas ou tiver ideias para melhorar, abra uma issue ou envie um pull request.

## Licen�a
Este projeto est� licenciado sob a [Licen�a MIT](LICENSE).

---

Se precisar de mais ajustes ou adi��es, � s� avisar!