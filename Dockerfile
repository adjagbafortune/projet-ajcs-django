# Utiliser l'image officielle Python comme base
FROM python:3.11-slim

# Définir un répertoire de travail pour l'application
WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    default-libmysqlclient-dev \
    libssl-dev \
    && apt-get clean

# Copier le fichier des dépendances (requirements.txt) dans le conteneur
COPY requirements.txt /app/

# Installer les packages Python dans l'environnement du conteneur
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code source
COPY . /app/