# SpetsChecker 🇷🇺

**SpetsChecker** est un outil de vérification `email:motdepasse` conçu pour cibler une URL de connexion personnalisée. Il permet :

- Chargement d'une combo `email:pass`
- Test des identifiants via une URL définie
- Utilisation de proxies pour éviter les bannissements
- Envoi automatique des **HITS** via Telegram
- Résultats triés (`hits.txt`, `bads.txt`, `errors.txt`)

## Installation

```bash
git clone https://github.com/votre-utilisateur/SpetsChecker.git
cd SpetsChecker
pip install -r requirements.txt
```

## Configuration

Créez un fichier `.env` à la racine du projet et remplissez avec :

```
TARGET_URL=https://example.com/login
TELEGRAM_BOT_TOKEN=VotreTokenIci
TELEGRAM_USER_ID=1200933877
```

Ajoutez vos combos dans `data/combo.txt`  
Ajoutez vos proxies dans `data/proxies.txt`

## Exécution

```bash
python main.py
```

💥 Les HITS seront envoyés à votre Telegram automatiquement !

## Avertissement

Ce projet est uniquement à des fins éducatives. Utilisez-le de manière responsable.
