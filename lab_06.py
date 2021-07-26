"""
Watching Start Wars Episodes on NodeMCU
>>Connect NodeMCU Internet
>>Download Asciimation
>>Display

NodeMCU connect to Internet
    ~ESP8266 WiFi based Chip with UART interfaace
    ~802.11b/g/n Protocal
    ~Integrated TCP/IP stact
    ~ON-chip SRAM

SSID -> Name for Wireless Network
IP -> Software level id for node
MAC -> Hardware level id for node
AP -> NodeMCU can also be mode as Access Point

Medium Blog : https://medium.com/@stestagg/playing-star-wars-on-the-esp8266-with-micropython-5f175fe7b755
"""
import network
import socket


def connect_to_ap():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to Network")
        wlan.connect('Mi-Fi', 'Pratik@124')
        while not wlan.isconnected():
            pass
    #print("Network Config: ", wlan.config())


def watch_starwars():
    addr_info = socket.getaddrinfo("towel.blinkenlights.nl", 23)
    addr = addr_info[0][-1]
    s = socket.socket()
    s.connect(addr)
    while True:
        data = s.recv(500)
        print(str(data, 'utf8'), end=' ')


def main():
    connect_to_ap()
    watch_starwars()


if __name__ == '__main__':
    print("Get Ready")
    main()
