from Manager import VehicleManager
from Model import Vehicle


manager = VehicleManager(url="https://test.tspb.su/test-task")
# Получение списка всех автомобилей
manager.get_vehicles()
# Получение списка автомобилей, у которых поле name равно 'Toyota'
manager.filter_vehicles(params={"name": "Toyota"})
# Получение автомобиля с id=1
manager.get_vehicle(vehicle_id=1)
# Добавление нового автомобиля в базу данных
manager.add_vehicle(
    vehicle=Vehicle(
        name='Toyota',
        model='Camry',
        year=2021,
        color='red',
        price=21000,
        latitude=55.753215,
        longitude=37.620393
    )
)
# Изменение информации об автомобиле с id=1
manager.update_vehicle(
        vehicle=Vehicle(
        name='Toyota',
        id=1,
        model='Camry',
        year=2021,
        color='red',
        price=21000,
        latitude=55.753215,
        longitude=37.620393
     )
 )
# Удаление автомобиля с id=1
manager.delete_vehicle(id=1)
manager.get_vehicle(vehicle_id=1)
 # Расчет расстояния между автомобилями с id=1 и id=2
manager.get_distance(id1=1, id2=2)
# Нахождение ближайшего автомобиля к автомобилю с id=1
manager.get_nearest_vehicle(id=1)