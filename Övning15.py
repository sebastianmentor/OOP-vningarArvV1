import random
import time

class Sensor:
    def mäta(self):
        return "Sensordata"
    
    def kalibrera(self):
        raise NotImplementedError
    
class Temperatursensor(Sensor):

    def mäta(self):
        return f"{random.randint(-30, 50)} grader!"
    
    def kalibrera(self):
        print("Kalibrera temperatursensorn!")
        print("Kalibrering börjar:", end='')
        for sec in range(10):
            time.sleep(0.2)
            print("#", end='', flush=True)
        print("\nKalibrering klar")
    
class Fuktighetsensor(Sensor):

    def mämäta(self):
        return f"{random.randint(0,100)}% fuktighet!"
    
    def kalibrera(self):
        print("Kalibrera fuktighetssensorn!")
        print("Kalibrering börjar:", end='')
        for sec in range(10):
            time.sleep(0.5)
            print("#", end='',flush=True)
        print("\nKalibrering klar")


t = Temperatursensor()
t.kalibrera()
f = Fuktighetsensor()
f.kalibrera()