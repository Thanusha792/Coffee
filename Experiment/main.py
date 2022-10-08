from Coffee.apiService import ApiService
from Coffee_Controller.hot_coffee_controller import response_controller
from Coffee_service.CoffeeSerializaton import CoffeeSerialization
from config import COFFEE



def main():
    #print(iced_coffee.read()) 
    coffeeApi = ApiService(COFFEE.API_BASE_URI)
    coffeeApi.get(COFFEE.END_POINT)
    





if __name__ == '__main__':
    main()


