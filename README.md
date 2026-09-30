# Atelier MongoDB — E-commerce

## Objectif

Découvrir MongoDB avec un dataset e-commerce, pratiquer le CRUD, utiliser les opérateurs de recherche, réaliser des agrégations et créer un index.

Durée de la démonstration : **20 minutes en binôme**.

## Téléchargements officiels

| Outil | Rôle | Source officielle |
|---|---|---|
| MongoDB Community Server | Serveur qui stocke les données | [Télécharger MongoDB Community Server](https://www.mongodb.com/try/download/community) |
| MongoDB Shell (`mongosh`) | Exécuter des commandes MongoDB | [Télécharger MongoDB Shell](https://www.mongodb.com/try/download/shell) |
| Python | Exécuter le notebook | [Télécharger Python](https://www.python.org/downloads/) |
| Visual Studio Code | Ouvrir et exécuter le projet | [Télécharger VS Code](https://code.visualstudio.com/Download) |

Dans VS Code, installer les extensions **Python** et **Jupyter**.

## Installation Python

Ouvrir PowerShell dans le dossier du projet :

```powershell
python -m pip install pymongo ipykernel
```

`pymongo` permet à Python de communiquer avec MongoDB. `ipykernel` permet d'exécuter les cellules du notebook.

## Structure du projet

```text
MongoDB-Workshop/
├── Atelier_MongoDB_20min.ipynb
├── README.md
└── data/
    ├── clients.json
    ├── produits.json
    ├── commandes.json
    └── ventes.json
```

| Fichier | Contenu |
|---|---|
| `clients.json` | 6 clients |
| `produits.json` | 8 produits |
| `commandes.json` | 15 commandes |
| `ventes.json` | Une ligne par produit vendu, préparée pour simplifier les agrégations |

Les fichiers JSON sont lisibles par une personne. MongoDB stocke les documents au format BSON.

## Démarrer MongoDB

MongoDB doit fonctionner avant l'ouverture du notebook.

Dans PowerShell :

```powershell
mongosh
```

Dans mongosh :

```text
db.runCommand({ ping: 1 })
use ecommerce
db.createCollection("clients")
db.createCollection("produits")
db.createCollection("commandes")
show dbs
show collections
```

Si une collection existe déjà, ne pas répéter sa commande `createCollection`.

## Exécuter le notebook

1. Ouvrir le dossier `MongoDB-Workshop` dans VS Code.
2. Ouvrir `Atelier_MongoDB_20min.ipynb`.
3. Cliquer sur **Select Kernel** et choisir Python.
4. Exécuter les cellules dans l'ordre avec **Shift + Entrée**.

Les cellules d'import commencent par vider les collections avant de réinsérer le dataset. Cela permet de relancer le notebook sans erreur de `_id` dupliqué.

## Partie 1 — premier membre du binôme

Durée : **10 minutes**.

- Installation et connexion.
- Création de la base et des collections dans mongosh.
- Import des fichiers JSON.
- `insertOne()` / `insertMany()`.
- `findOne()` / `find()`.
- `updateOne()` / `updateMany()`.
- `deleteOne()` / `deleteMany()`.
- Opérateurs `$gt`, `$gte`, `$lt`, `$lte`, `$in`, `$ne`, `$and`, `$or` et `$exists`.

Dans Python, les mêmes méthodes utilisent des underscores : `insert_one()`, `find_one()`, `update_many()`, etc.

## Partie 2 — deuxième membre du binôme

Durée : **10 minutes**.

- `$match` pour filtrer.
- `$group` et `$sum` pour calculer.
- `$sort` pour trier.
- `$limit` pour limiter les résultats.
- `$lookup` pour relier deux collections.
- `$project` pour choisir les champs affichés.
- Produits les plus vendus.
- Chiffre d'affaires par catégorie.
- Meilleurs clients.
- Ventes par mois.
- Création et utilisation d'un index.

## Résultats attendus

| Analyse | Résultat principal |
|---|---|
| Produit le plus vendu | Stylo — 14 unités |
| Meilleur client | Amina — 1 270 MAD |
| Chiffre d'affaires total | 5 720 MAD |
| Commandes payées | 14 |
| Index sur `client_id` | 15 documents examinés avant, 3 après |

## Documentation officielle

- [Bases et collections](https://www.mongodb.com/docs/manual/core/databases-and-collections/)
- [MongoDB Shell](https://www.mongodb.com/docs/mongodb-shell/)
- [CRUD avec PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/crud/)
- [Agrégations avec PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/aggregation/)
- [Index avec PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/indexes/)
