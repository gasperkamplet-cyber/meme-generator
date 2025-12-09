# 1. Osnovna slika Python
FROM python:3.12-slim

# 2. Nastavi delovni direktorij v containerju
WORKDIR /app

# 3. Kopiraj vse datoteke iz projekta v container
COPY . .

# 4. Namesti odvisnosti
RUN pip install --no-cache-dir -r requirements.txt

# 5. Nastavi okoljsko spremenljivko za port
ENV PORT=5000

# 6. Odpri port 5000
EXPOSE 5000

# 7. Zaženi aplikacijo
CMD ["python", "app.py"]
