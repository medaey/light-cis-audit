#!/bin/bash

# run-audit.sh — Lance l'audit CIS avec l'environnement virtuel Python

set -e

GREEN='\033[0;32m'
NC='\033[0m'

# Vérifie erreur fréquente d'argument
if [[ "$*" == *"--outputfile"* ]]; then
  echo -e "❌ Utilisez --output-file (avec un tiret) au lieu de --outputfile"
  exit 1
fi

echo -e "${GREEN}🚀 Initialisation de l'environnement...${NC}"

if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate

echo -e "${GREEN}📦 Installation des dépendances...${NC}"
pip install --break-system-packages -r requirements.txt

echo -e "${GREEN}🔍 Lancement de l'audit...${NC}"
sudo python3 main.py "$@"
