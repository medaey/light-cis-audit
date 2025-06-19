#!/bin/bash

set -e

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

if [[ "$*" == *"--outputfile"* ]]; then
  echo -e "${RED}❌ Utilisez --output-file (avec un tiret) au lieu de --outputfile${NC}"
  exit 1
fi

if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python3 n'est pas installé ou n'est pas dans le PATH.${NC}"
    echo "Veuillez installer Python 3.6+ (avec le module venv et pip) avant d'exécuter ce script."
    exit 1
fi

echo -e "${GREEN}🚀 Initialisation de l'environnement...${NC}"

if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate

if ! command -v pip &> /dev/null; then
    echo -e "${RED}❌ pip n'est pas disponible dans l'environnement virtuel.${NC}"
    echo "Veuillez installer pip dans votre environnement Python."
    echo
    echo "Sur Debian/Ubuntu, vous pouvez installer les paquets nécessaires avec :"
    echo "  sudo apt install python3-venv python3-pip"
    echo
    echo "Sur Red Hat/CentOS/AlmaLinux, vous pouvez installer les paquets avec :"
    echo "  sudo dnf install python3-venv python3-pip"
    echo "ou (selon la version) :"
    echo "  sudo yum install python3-venv python3-pip"
    exit 1
fi

echo -e "${GREEN}📦 Installation des dépendances...${NC}"
pip install --break-system-packages -r requirements.txt

echo -e "${GREEN}🔍 Lancement de l'audit...${NC}"
sudo python3 main.py "$@"
