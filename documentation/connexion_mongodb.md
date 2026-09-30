# Connexion Python à MongoDB local

## Objectif de cette étape

Vérifier que Python peut joindre le serveur MongoDB installé sur ce PC. Le fichier `conn.py` est **en lecture seule** : il ne crée aucune base, collection ou donnée. Les fichiers JSON du dossier `data` ne sont pas importés à cette étape.

## Les trois éléments à distinguer

| Élément | Rôle |
| --- | --- |
| `mongod` | Serveur MongoDB qui conserve les données et attend les connexions. |
| PyMongo | Bibliothèque Python qui permet de communiquer avec MongoDB. |
| `MongoClient` | Objet PyMongo qui représente la connexion utilisée par le script. |

Le script utilise `mongodb://localhost:27017/`. `localhost` désigne **le même ordinateur** que celui qui exécute Python. `27017` est le port local par défaut de MongoDB. Ce choix convient à notre installation locale ; il faudrait modifier l'adresse si le serveur tournait ailleurs ou sur un autre port. [Source : documentation MongoDB sur les connexions locales](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/connection-targets/).

## Exécuter le test

1. Vérifier que le serveur `mongod` fonctionne.
2. Ouvrir PowerShell dans le dossier `MongoDB-Workshop`.
3. Exécuter `python .\conn.py`.

Sur ce PC, PyMongo est déjà installé. Sur un autre PC, si Python affiche `No module named 'pymongo'`, installer la bibliothèque avec `python -m pip install pymongo`. [Source : guide PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/get-started/).

## Lire le code, ligne par ligne

1. `from pymongo import MongoClient` importe l'outil de connexion officiel pour Python.
2. `from pymongo.errors import PyMongoError` permet de présenter un message lisible en cas d'erreur MongoDB.
3. `uri` contient l'adresse du serveur local ; `nom_base` contient le nom de la base que nous utiliserons plus tard.
4. `with MongoClient(uri, serverSelectionTimeoutMS=5000) as client` prépare le client. Le bloc `with` ferme ce client à la fin. Le délai de cinq secondes évite d'attendre trop longtemps si le serveur ne répond pas.
5. `client.admin.command("ping")` demande une réponse au serveur. C'est cette commande qui **vérifie réellement** la connexion ; la seule création de l'objet `MongoClient` ne suffit pas. [Source : PyMongo, création et fermeture du client](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/mongoclient/).
6. `db = client[nom_base]` sélectionne un objet représentant la base `ecommerce`. **Cette ligne ne crée pas la base sur le serveur.**
7. `client.list_database_names()` vérifie si `ecommerce` existe déjà. Si oui, `db.list_collection_names()` affiche ses collections. Ces opérations lisent l'état du serveur.
8. Le bloc `except` explique l'erreur de connexion et termine le script avec un code d'échec.

## Résultat attendu à ce stade

Lors de la vérification du 29 septembre 2026, le serveur local a répondu au `ping`, mais la base `ecommerce` n'existait pas encore. Le script doit donc annoncer une connexion réussie, puis préciser que la base n'a pas encore été créée. Si la base est créée plus tard, le même script indiquera qu'elle existe et affichera ses collections.

## Phrase courte pour expliquer à un camarade

> J'utilise PyMongo pour contacter le serveur MongoDB de mon ordinateur. Le `ping` confirme la connexion. Sélectionner le nom `ecommerce` ne crée pas la base : nous la créerons à l'étape suivante.
