# Meme Generator

## Opis
Aplikacija omogoča nalaganje slike, vnos zgornjega in spodnjega besedila ter generiranje mema.

## Tehnologije
- Python 3.12
- Flask
- Pillow

## Zagon z Dockerjem
```bash
docker build -t meme-generator .
docker run -p 5000:5000 meme-generator
