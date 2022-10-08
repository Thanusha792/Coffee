import requests
from Coffee_Controller.hot_coffee_controller import response_controller
# API service class to request coffee api for using get method.
class ApiService :
    baseurl = ""
# constructore with one parameter accepting base uri
    def __init__(self, uri):
        self.baseurl = uri

# Get method to get the list of hot coffee
    def get(self,endpoint):
        try:
            response = requests.get(self.baseurl+endpoint)
            response_controller(response)
        except requests.exceptions.Timeout:
            print("Timeout")
        
        
        




      


        
