# IoT Agro

## Descrição
Projeto de automação agrícola utilizando ESP32 para monitoramento de temperatura e umidade em tempo real com integração via MQTT.

## Estrutura do Projeto
- **ESP32** com sensor DHT11 para medir temperatura e umidade.
- **MQTT** para enviar os dados para um servidor ou dashboard.

## Como Usar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seuperfil/iot-agro.git
   cd iot-agro
2. Suba os arquivos para o ESP32 utilizando um IDE como Thonny.
3. Configure sua rede Wi-Fi em 'main.py':
    ```markdown
   ```python
    WIFI_SSID = "sua_rede_wifi"
    WIFI_PASSWORD = "sua_senha_wifi"
4. Execute o código no ESP32 e visualize os dados publicados no broker MQTT.


## Conteúdo dos Arquivos
1. sensors/__init__.py
   ```markdown
    Deixe este arquivo vazio. Ele apenas transforma o diretório sensors em um módulo Python.

2. sensors/dht_sensor.py
   ```markdown
   Código para gerenciar o sensor DHT11 (temperatura e umidade):

3. sensors/mqtt_client.py
   ```markdown
   Código para gerenciar a comunicação MQTT

4. main.py
   ```markdown
   Código principal para integrar os sensores e o MQTT:





   
