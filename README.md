# JS SCAN - JavaScript Library Security Scanner

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/yourusername/scanJs)
[![Python](https://img.shields.io/badge/python-3.x-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)

**JS SCAN** est un outil de sécurité défensif permettant de scanner les bibliothèques JavaScript utilisées sur un site web et d'identifier les vulnérabilités connues (CVE) ainsi que les versions obsolètes.

## 🎯 Fonctionnalités

- ✅ **Détection automatique** des bibliothèques JavaScript sur un site web
- 🔍 **Identification des versions** actuelles et dernières disponibles
- 🛡️ **Scan de vulnérabilités** via l'API Snyk
- 📊 **Rapport détaillé** avec affichage coloré dans le terminal
- ⚡ **Interface CLI simple** et intuitive

## 📋 Prérequis

- Python 3.x
- Clé API Snyk (gratuite disponible sur [snyk.io](https://snyk.io))
- Connexion Internet

## 🔧 Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/yourusername/scanJs.git
cd scanJs
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

3. Configurez votre clé API Snyk :
```bash
export SNYK_API_KEY="votre_clé_api_snyk"
```

## 🚀 Utilisation

### Commande de base

```bash
python main.py -u https://example.com
```

### Options disponibles

- `-u, --url` : URL du site web à scanner (obligatoire)
- `-p, --path` : Chemin spécifique vers les bibliothèques JavaScript (optionnel)

### Exemple

```bash
python main.py -u https://votresite.com
```

## 📊 Exemple de sortie

```
_______________________________________________________________

       _    _____      _____    _____              _   _
      | |  / ____|    / ____|  / ____|     /\     | \ | |
      | | | (___     | (___   | |         /  \    |  \| |
  _   | |  \___ \     \___ \  | |        / /\ \   | . ` |
 | |__| |  ____) |    ____) | | |____   / ____ \  | |\  |
  \____/  |_____/    |_____/   \_____| /_/    \_\ |_| \_|

         JS Library Security Scanner by Amel Sid
                 Version 1.0.0
_______________________________________________________________

┏━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃ Lib        ┃ Version  ┃ CVE                ┃ New Version┃ Reco               ┃
┡━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ jquery     │ 3.3.1    │ CVE-2020-11022     │ 3.7.1      │ Update recommended │
│ react      │ 16.8.0   │ N/A                │ 18.2.0     │ Update recommended │
└────────────┴──────────┴────────────────────┴────────────┴────────────────────┘
```

## 🏗️ Architecture du projet

```
scanJs/
│
├── main.py                    # Point d'entrée principal
├── js_detector.py             # Détection des bibliothèques JS
├── version_checker.py         # Vérification des versions via npm
├── vulnerability_finder.py    # Recherche de CVE via Snyk
├── web_scraper.py            # Scraping du site web
├── utils.py                  # Utilitaires et affichage des résultats
├── config.py                 # Configuration
└── requirements.py           # Dépendances Python
```

## 🔍 Fonctionnement

1. **Scraping** : Le script analyse le HTML du site cible pour extraire toutes les balises `<script>`
2. **Extraction** : Les noms et versions des bibliothèques sont extraits des URLs des scripts
3. **Vérification** : Les dernières versions sont récupérées depuis le registre npm
4. **Analyse de sécurité** : Les vulnérabilités sont identifiées via l'API Snyk
5. **Rapport** : Un tableau détaillé est affiché avec les recommandations

## 📦 Dépendances principales

- `requests` : Requêtes HTTP
- `beautifulsoup4` : Parsing HTML
- `rich` : Affichage riche dans le terminal

## 🛡️ Sécurité

Cet outil est conçu à des **fins défensives uniquement** :
- Audit de sécurité de vos propres sites web
- Identification proactive des vulnérabilités
- Mise en conformité avec les bonnes pratiques de sécurité

⚠️ **N'utilisez cet outil que sur des sites dont vous êtes propriétaire ou pour lesquels vous avez une autorisation explicite.**

## 👤 Auteur

**Amel Sid**

## 📝 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Push vers la branche
5. Ouvrir une Pull Request

## 📧 Support

Pour toute question ou problème, ouvrez une issue sur GitHub.

---

⭐ Si ce projet vous est utile, n'hésitez pas à lui donner une étoile !
