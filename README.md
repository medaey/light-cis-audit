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
