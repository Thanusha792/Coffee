import csv
import json
import datetime
import logging

from requests import Response
from config.COFFEE import ICED_COFFEE_PATH
from Models.CoffeeDeserializer import CoffeeDeserializer

from Coffee_service.CoffeeSerializaton import CoffeeSerialization
# Get the responce and work accordingly
def response_controller(response: Response):
    if  response.status_code== 200:
            iced_coffee_list= CoffeeDeserializer.read(CoffeeDeserializer,ICED_COFFEE_PATH)
            hot_coffee_Json_object=response.json()
            hot_coffee_Response_text=json.dumps(hot_coffee_Json_object)
            hot_coffee_Response_dict=json.loads(hot_coffee_Response_text)
            Current_time=datetime.datetime.now().astimezone().replace(microsecond=0).isoformat().replace(':', '_')+"_-_hot.json"
            with open(Current_time, 'w') as output:
               json.dump(hot_coffee_Json_object, output)
            hot_coffee_list=CoffeeSerialization.json_to_list(CoffeeSerialization,hot_coffee_Response_dict)
            coffee_list=iced_coffee_list+hot_coffee_list
            header_names = ['title', 'description', 'ingredients','image','id']
            with open('final_coffee.csv', 'w') as f:
                writer=csv.writer(f)
                writer.writerow(header_names)
                for doc in coffee_list:
                    writer.writerow(doc)

    else:
        logging.basicConfig(filename="run.log",level=logging.error)
        logging.error(Current_time+" | "+response.status_code+" | Coffee api unreachable")
            

        