# 🔒 light-cis-audit

**light-cis-audit** est un outil d’audit système **léger**, **modulaire** et **auto-hébergeable**, conçu pour vérifier rapidement la sécurité de la configuration des serveurs Linux (Debian/Ubuntu), en s’inspirant des recommandations CIS (Center for Internet Security) sans la lourdeur des outils traditionnels.

---

## 🎯 Objectifs

- ✅ Vérifier les configurations critiques (SSH, utilisateurs, firewall, permissions…)
- 📋 Générer des rapports clairs et lisibles (Markdown, JSON, HTML à venir)
- 🧩 Fournir une architecture simple pour écrire et maintenir ses propres checks
- 🚫 Zéro dépendance lourde, pas de modification du système (read-only)

---

## 🛠️ Fonctionnalités

- 🔐 Vérification de la configuration SSH (port, root login, protocol, etc.)
- 👥 Détection des comptes sans mot de passe
- 🔥 État du pare-feu (UFW, iptables)
- 🧱 Analyse des fichiers à permissions spéciales (SUID)
- 🧪 Résultats catégorisés : `PASS`, `FAIL`, `WARN`, `INFO`
- 🖥️ Interface en ligne de commande minimaliste

---

## 🚀 Installation

```bash
git clone https://github.com/medaey/light-cis-audit.git
cd light-cis-audit
pip install -r requirements.txt
```

💡 L’outil nécessite Python 3.6+ et utilise les utilitaires Linux classiques (grep, awk, find, etc.)

## ⚡ Usage
### Lancer tous les checks (par défaut en JSON)
```bash
sudo python3 main.py
```

### Lancer des checks ciblés (exemple SSH + utilisateurs)
```bash
sudo python3 main.py --check ssh users
```

### Choisir le format de sortie (`json` ou `markdown`)
```bash
sudo python3 main.py --output markdown
sudo python3 main.py --output json
```

### Sauvegarder le rapport dans un fichier
```bash
sudo python3 main.py --output markdown --output-file rapport.md
```

## 📊 Exemple de sortie JSON

```json
[
  {
    "id": "SSH-001",
    "description": "SSH root login must be disabled",
    "result": "PASS",
    "details": "PermitRootLogin is set to no"
  },
  {
    "id": "USER-002",
    "description": "No user account without password",
    "result": "FAIL",
    "details": "User 'backup' has no password set"
  }
]
```

## 📁 Arborescence
```bash
light-cis-audit/
├── audit/           # Modules pour chaque domaine (ssh, users, etc.)
├── reports/         # Générateurs de rapports (json, markdown...)
├── tests/           # Tests unitaires
├── main.py          # CLI principale
├── requirements.txt
└── README.md
```

## ✅ Roadmap

- [ ] Option --fix pour corriger automatiquement certains problèmes
- [ ] Rapport HTML interactif
- [ ] Profils personnalisables (cis, minimal, custom)
- [ ] Support pour RedHat/CentOS


## 🤝 Contribution
Les contributions sont les bienvenues !
Suggestions, issues et pull requests sont ouvertes à tous.

## 🛡️ Disclaimer
Ce projet est fourni à des fins **d’audit rapide.**
Il **ne remplace pas un audit complet** réalisé par un professionnel de la sécurité.

## 👤 Auteur
Projet développé par @medaey