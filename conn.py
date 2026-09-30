"""Vérifie la connexion à MongoDB local sans créer de base ni de collection."""

from pymongo import MongoClient
from pymongo.errors import PyMongoError


uri = "mongodb://localhost:27017/"
nom_base = "ecommerce"

try:
    # Le bloc "with" fermera le client à la fin du test.
    with MongoClient(uri, serverSelectionTimeoutMS=5000) as client:
        # MongoClient seul ne prouve pas que le serveur répond : ping le vérifie.
        client.admin.command("ping")
        print("MongoDB local : connexion OK.")

        # Cette ligne sélectionne un nom de base sans la créer.
        db = client[nom_base]
        print(f"Base choisie : {db.name}")

        if nom_base in client.list_database_names():
            print("Base presente sur le serveur.")
            print(f"Collections : {db.list_collection_names()}")
        else:
            print("Base absente du serveur : ce script ne la cree pas.")

except PyMongoError as erreur:
    print("Connexion impossible : mongod doit fonctionner sur localhost:27017.")
    print(f"Detail : {erreur}")
    raise SystemExit(1)
