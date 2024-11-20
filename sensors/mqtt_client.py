from umqtt.simple import MQTTClient
import json

class MQTTClientWrapper:
    def __init__(self, client_id, broker, topic):
        self.client = MQTTClient(client_id, broker)
        self.topic = topic
    
    def connect(self):
        try:
            self.client.connect()
            print(f"Conectado ao broker MQTT: {self.client.server}")
        except Exception as e:
            print(f"Erro ao conectar ao MQTT: {e}")
    
    def publish(self, data):
        try:
            payload = json.dumps(data)
            self.client.publish(self.topic, payload)
            print(f"Dados publicados: {payload}")
        except Exception as e:
            print(f"Erro ao publicar dados: {e}")
