"""
Temperature & Humidity Sensor (DHT11)
Communication: 1 Wire-Serial

Temperature Sensor:
    >> NTC Thermistor (Negative Temperature Coefficient)
    >> Resistance inversely proportional to Temperature
Humidity Sensor:
    >> Capacitive Measurement

Speaking to DHT11:
RQST: Request to DHT11
RESP: Response from DHT11
Data: Data from DHT11
EOF: End of Frame from DHT11

Data: 5 Bytes(40 bits)
| Integral | Decimal | Integral | Decimal | check sum |
|      Humidity      |    Temperature     |

"""
import machine
import dht

while True:
    d = dht.DHT11(machine.Pin(4))
    d.measure()
    temp = d.temperature()
    humd = d.humidity()
    print("Temperature :", temp, "Humidity :", humd)