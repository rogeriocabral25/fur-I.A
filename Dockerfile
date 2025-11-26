# Usa uma imagem leve do Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos para o container
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que o Streamlit usa
EXPOSE 8080

# Comando para rodar o app
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]