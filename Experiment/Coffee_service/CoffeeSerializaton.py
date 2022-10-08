from Models.CoffeeDeserializer import CoffeeDeserializer
class CoffeeSerialization:
    def json_to_list(cls, coffee_json):
        list=[]
        for i in coffee_json:
            obje=[]
            obje.append(i['title'])
            obje.append(i['description'])
            obje.append(i['ingredients'])
            obje.append(i['image'])
            obje.append(i['id'])
            list.append(obje)
        return list 