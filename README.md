# Docker_Python
Rodar Script Python em via Docker

# Build Imagem
docker build -t my-python-app .

# Iniciar Container
docker run -v /Users/frudek/Documents/Developer/Docker/python:/app my-python-app
