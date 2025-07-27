FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos do projeto
COPY . .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8501
# Define comando padrão (ajustável)
#CMD ["python", "app.py"]
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
