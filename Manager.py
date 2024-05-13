import requests
from math import radians, cos, sin, atan2, sqrt
from Model import Vehicle

class VehicleManager:
    def __init__(self, url):
        self.url = url

    def get_vehicles(self):
        response = requests.get(f"{self.url}/vehicles")
        vehicles = [self._create_vehicle(data) for data in response.json()]
        print(f'{response} Получил данные')
        return vehicles

    def filter_vehicles(self, params):
        vehicles = self.get_vehicles()
        for key,value in params.items():
            vehicles = [v for v in vehicles if v.__dict__[key]==value]
        print('Фильтрация успешна')
        return vehicles

    def get_vehicle(self, vehicle_id):
        response = requests.get(f"{self.url}/vehicles/{vehicle_id}")
        vehicle = self._create_vehicle(response.json())
        print(f'{response} Получил данные по id')
        return vehicle

    def add_vehicle(self, vehicle):
        response = requests.post(f"{self.url}/vehicles", json=vehicle.__dict__)
        print(f'{response} Добавил данные - {vehicle}')
        return self._create_vehicle(response.json())

    def update_vehicle(self, vehicle):
        response = requests.put(f"{self.url}/vehicles/{vehicle.id}", json=vehicle.__dict__)
        print(f'{response} Обновил данные - {vehicle}')
        return self._create_vehicle(response.json())

    def delete_vehicle(self, id):
        requests.delete(f"{self.url}/vehicles/{id}")
        print(f' Удалил данные - id:{id}')

    def get_distance(self, id1, id2):
        vehicle1 = self.get_vehicle(id1)
        vehicle2 = self.get_vehicle(id2)
        distance = self._calculate_distance(vehicle1.latitude, vehicle1.longitude, vehicle2.latitude, vehicle2.longitude)
        print(f'Дистанция между автомобилями {id1} и {id2} равна {distance}')
        return distance

    def get_nearest_vehicle(self, id):
        vehicles = self.get_vehicles()
        target_vehicle = self.get_vehicle(id)
        nearest_vehicle = min(vehicles, key=lambda v: self._calculate_distance(target_vehicle.latitude, target_vehicle.longitude, v.latitude, v.longitude))
        print(f'Ближайшим автомобилем является {nearest_vehicle} к автомобилю с {id}')
        return nearest_vehicle

    def _create_vehicle(self, data):
        return Vehicle(
            id=data["id"],
            name=data['name'],
            model=data["model"],
            year=data["year"],
            color=data["color"],
            price=data["price"],
            latitude=data["latitude"],
            longitude=data["longitude"]
        )

    def _calculate_distance(self, lat1, lon1, lat2, lon2):
        R = 6371000  # Радиус Земли в метрах
        phi1 = radians(lat1)
        phi2 = radians(lat2)
        delta_phi = radians(lat2 - lat1)
        delta_lambda = radians(lon2 - lon1)

        a = sin(delta_phi / 2) * sin(delta_phi / 2) + cos(phi1) * cos(phi2) * sin(delta_lambda / 2) * sin(delta_lambda / 2)
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return R * c