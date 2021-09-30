import socket

import requests


def get_current_ip_address():
    """This retrieves the IP address of the default route."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(('10.255.255.255', 1))
        ip = sock.getsockname()[0]
    finally:
        sock.close()
    return ip


def is_port_open(ip_address, port=80):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result_of_check = sock.connect_ex((ip_address, port))

        if result_of_check == 0:
            return True
        else:
            return False
    finally:
        sock.close()


def detect_esp32_webserver(ip_range):
    socket.setdefaulttimeout(0.3)
    session = requests.Session()

    print('Trying to detect ESP32 webserver...')
    try:
        for i in range(1, 256):
            print('.', end='', flush=True)
            ip_address = ip_range.format(i)
            if is_port_open(ip_address):
                response = session.get('http://{}/hi'.format(ip_address))
                if response.text == 'Hello SJSU':
                    return ip_address
    finally:
        print()

if __name__ == '__main__':
    ip_address = get_current_ip_address()
    print('Current IP address: {}'.format(ip_address))
    ip_range = ip_address[0:ip_address.rindex('.')] + '.{}'

    print('Range for ESP32 detection: {}'.format(ip_range.format('1/255')))
    esp32_ip_address = detect_esp32_webserver(ip_range)
    print('Found ESP32 server: {}'.format(esp32_ip_address))
