from typing import List
import json

# CoffeeDeserialization class for converting json to model.
class CoffeeDeserializer:
    title = ""
    description = ""
    ingredients = []
    image = ""
    id = -1
    
    def __init__(self, title, description, ingredients, image, id):
        self.title = title
        self.description = description
        self.ingredients = ingredients
        self.image = image
        self.id = id
        
    def __repr__(self):
        return "CoffeeDeserializer({},{},{},{},{})".format(self.title, self.description, self.ingredients, self.image, self.id)
    
    def read(cls, filepath):
        list=[]
        f=open(filepath)
        iced_coffee=json.load(f)
        for i in iced_coffee:
            obje=[]
            obje.append(i['title'])
            obje.append(i['description'])
            obje.append(i['ingredients'])
            obje.append(i['image'])
            obje.append(i['id'])
            list.append(obje)
        f.close()
        return list
