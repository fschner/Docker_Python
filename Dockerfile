# Use a imagem oficial do Python
FROM python:3.9

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Instale o pacote "cryptography" para suportar autenticação no MySQL
RUN pip install cryptography

# Copie o script Python para o diretório de trabalho no contêiner
COPY script.py /app/script.py

# Instale as dependências necessárias (pode incluir outras bibliotecas)
RUN pip install pymysql openpyxl

# Execute o script Python
CMD python script.py





