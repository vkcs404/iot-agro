import time
from sensors.dht_sensor import DHTSensor
from sensors.mqtt_client import MQTTClientWrapper

# Configurações
WIFI_SSID = "sua_rede_wifi"
WIFI_PASSWORD = "sua_senha_wifi"
MQTT_BROKER = "broker.mqtt-dashboard.com"
MQTT_TOPIC = "iot_agro/sensor_data"
DHT_PIN = 4

# Conectar ao Wi-Fi
def connect_wifi():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    while not wlan.isconnected():
        time.sleep(1)
    print("Conectado ao Wi-Fi:", wlan.ifconfig())

# Inicializar sensores e MQTT
def main():
    connect_wifi()
    dht_sensor = DHTSensor(DHT_PIN)
    mqtt_client = MQTTClientWrapper("esp32_iot_agro", MQTT_BROKER, MQTT_TOPIC)
    mqtt_client.connect()

    while True:
        data = dht_sensor.read_data()
        if data:
            mqtt_client.publish(data)
        time.sleep(10)

# Executar o programa
if __name__ == "__main__":
    main()
