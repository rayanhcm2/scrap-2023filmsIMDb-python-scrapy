# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import sqlite3
from itemadapter import ItemAdapter


class FilmsimdbPipeline:
    def process_item(self, item, spider):
        return item
    
class DatabasePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect('Films.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS Films")
        self.cursor.execute("CREATE TABLE if not exists Films (Title TEXT,Image TEXT,Catégorie TEXT,Description TEXT,Rate TEXT,Réalisation TEXT,Scénario TEXT)")
    
    def close_spider(self, spider):
        self.conn.close()
    
    def process_item(self, item, spider):
        query = "INSERT INTO Films (title, image,Catégorie, Description, Rate, Réalisation, Scénario) VALUES (?, ?, ?, ?, ?, ?,?)"
        values = (item['title'], item['Image'], json.dumps(item['Catégorie']), item['description'], item['rate_IMDb'], item['Realisation'], item['Scénario'])
        self.cursor.execute(query, values)
        self.conn.commit()
        self.conn.commit()
        return item
