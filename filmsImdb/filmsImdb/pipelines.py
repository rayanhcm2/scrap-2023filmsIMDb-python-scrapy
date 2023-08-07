# Importer les modules nécessaires
import json
import sqlite3
from itemadapter import ItemAdapter

# Pipeline pour traiter les éléments de l'araignée
class FilmsimdbPipeline:
    def process_item(self, item, spider):
        # Renvoyer l'élément tel quel sans modification
        return item

# Pipeline pour enregistrer les données dans une base de données SQLite
class DatabasePipeline:
    def open_spider(self, spider):
        # Se connecter à la base de données et créer une table pour les films
        self.conn = sqlite3.connect('Films.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS Films")
        self.cursor.execute("CREATE TABLE if not exists Films (Title TEXT,Image TEXT,Catégorie TEXT,Description TEXT,Rate TEXT,Réalisation TEXT,Scénario TEXT)")
    
    def close_spider(self, spider):
        # Fermer la connexion à la base de données
        self.conn.close()
    
    def process_item(self, item, spider):
        # Préparer et exécuter la requête d'insertion dans la base de données
        query = "INSERT INTO Films (title, image, Catégorie, Description, Rate, Réalisation, Scénario) VALUES (?, ?, ?, ?, ?, ?, ?)"
        values = (item['title'], item['Image'], json.dumps(item['Catégorie']), item['description'], item['rate_IMDb'], item['Realisation'], item['Scénario'])
        self.cursor.execute(query, values)
        self.conn.commit()
        
        # Renvoyer l'élément tel quel pour le traitement ultérieur
        return item
