import machine
import dht

class DHTSensor:
    def __init__(self, pin):
        self.sensor = dht.DHT11(machine.Pin(pin))
    
    def read_data(self):
        try:
            self.sensor.measure()
            return {
                "temperature": self.sensor.temperature(),
                "humidity": self.sensor.humidity()
            }
        except Exception as e:
            print(f"Erro ao ler sensor DHT: {e}")
            return None
