# inheritance vs composition

# my solution
class Vehicle:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires

class Tires:
    def __init__(self, size):
        self.size = 0
        self.__pressure = 0

    @property
    def pressure(self):
        print("The pressue is: ", self.__pressure)
        return self.__pressure

    @pressure.setter
    def pressure(self, amount):
        self.__pressure += amount
        print("The pressure increased by: {} PSI".format(amount) )

class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.__state = False

    def start(self):
        self.__state = True
        print("Starting the Engine")

    def stop(self):
        self.__state = False
        print("Stopping the Engine")

    def get_state(self):
        if self.__state is False:
             print("Engine is Off")
             return self.__state
        elif self.__state is True:
            print("Engine is On")
            return self.__state
        else:
            #ideally should not execute this clauses
            return self.__state

electric_engine = Engine('electricity')
city_tires = Tires(15)
city_tires.pressure = 30
print(city_tires.pressure)

myVehicle = Vehicle(VIN="787", engine=electric_engine, tires=city_tires)

myVehicle.engine.start()
myVehicle.engine.get_state()
myVehicle.engine.stop()
myVehicle.engine.get_state()
myVehicle.tires.pressure += 5
myVehicle.tires.pressure

#their solution
# the main difference is that they kept the pressure property public in the Tires class
class Car:
    def __init__(self, VIN, engine, tires):
        self.VIN = VIN
        self.engine = engine
        self.tires = tires

class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def get_pressure(self):
        return self.pressure

    def pump(self, psi):
        self.pressure = psi

class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = 'off'

    def start(self):
        self.state = 'on'

    def stop(self):
        self.state = 'off'

    def get_state(self):
        return self.state

city_tires = Tires(15)
off_road_tires = Tires(18)

electric_engine = Engine('electric')
petrol_engine = Engine('electric')

city_car = Car('111A', electric_engine, city_tires)
all_terrain_car = Car('888S', petrol_engine, off_road_tires)

# prepare all_terrain_car for a rally
print('All-terrain car engine is', all_terrain_car.engine.get_state())
all_terrain_car.tires.pump(10)
all_terrain_car.engine.start()
print('All-terrain car engine is', all_terrain_car.engine.get_state())

# prepare city car for a shopping
print('City car engine is', city_car.engine.get_state())
city_car.tires.pump(3)
city_car.engine.start()
print('City car engine is', city_car.engine.get_state())
city_car.engine.stop()
print('City car engine is', city_car.engine.get_state())
