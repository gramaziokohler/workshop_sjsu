import argparse
import asyncio
import functools
import io
import itertools
import json
import os
import socket
import struct
import sys

import requests

BYTE_ORDER = '<'
PAYLOAD_FORMAT = 'Ic'


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


def is_lightbrush(ip_address, session=None):
    session = session or requests.Session()
    response = session.get('http://{}/hi'.format(ip_address), verify=False)
    return response.text == 'Hello SJSU'


def detect_esp32_webserver(ip_range):
    session = requests.Session()

    progress = '⠁⠂⠄⡀⢀⠠⠐⠈'
    for i in range(1, 256):
        print(' [{}]\r'.format(progress[i % len(progress)]), end='', flush=True)
        ip_address = ip_range.format(i)
        if is_port_open(ip_address):
            if is_lightbrush(ip_address, session):
                return ip_address


async def handle_tcp_request(callback, reader, writer):
    try:
        data = await reader.readline()
        value, _delim = struct.unpack(BYTE_ORDER + PAYLOAD_FORMAT, data)
        addr, port = writer.get_extra_info('peername')

        print(f' [ ] Received "{value}" from {addr}:{port}', end='', flush=True)
        callback(value)
        print(f' [✓]')

    finally:
        if writer:
            writer.close()


async def start_server(callback, port=9111):
    print(' [ ] Starting TCP server...\r', end='', flush=True)
    server = await asyncio.start_server(functools.partial(handle_tcp_request, callback), '0.0.0.0', port)
    addr, port = server.sockets[0].getsockname()
    print(f' [✓] Started TCP server on {addr}:{port}')

    async with server:
        await server.serve_forever()


def load_command_file(file):
    if not os.path.exists(file):
        print(f' [!] Cannot find file={file}')
        print('     Verify the file exists and is a valid JSON file.')
        sys.exit(1)

    with io.open(file, 'r') as fp:
        commands = json.load(fp)

        colors = list(itertools.chain(*(commands['colors'])))
        gradients = list(itertools.chain(*(commands['gradients'])))
        points3d = list(itertools.chain(*(commands['points3d'])))

    if len(colors) != len(gradients) or len(gradients) != len(points3d):
        print(' [!] Length of colors/gradients/points do not match between each other!')
        print('     Colors: {}, Gradients: {}, Points 3D: {}'.format(
            len(colors), len(gradients), len(points3d)))
        sys.exit(1)

    return dict(
        colors=colors,
        gradients=gradients,
        points3d=points3d,
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lightbrush proxy')
    parser.add_argument(
        'file', type=str, help='light painting file containing robot points and colors')
    parser.add_argument(
        '--ip', type=str, help='IP address of the lightbrush server. Leave empty for auto-detect')
    parser.add_argument(
        '--brightness', type=int, help='Integer between 0-255 indicating brightness of the LEDs', default=255)

    args = parser.parse_args()

    print()
    print('Lightbrush Proxy')
    print()

    print(' [ ] Loading commands file...\r', end='', flush=True)
    flat_data = load_command_file(args.file)
    print(' [✓] Loaded {} points/commands'.format(len(flat_data['points3d'])))

    ip_address = get_current_ip_address()
    print(' [✓] Local IP address: {}'.format(ip_address))

    socket.setdefaulttimeout(0.3)
    if not args.ip:
        ip_range = ip_address[0:ip_address.rindex('.')] + '.{}'
        print(' [✓] Lightbrush detection range: {}'.format(
            ip_range.format('1/255')))

        print(' [ ] Detecting Lightbrush server...\r', end='', flush=True)
        esp32_ip_address = detect_esp32_webserver(ip_range)
        if not esp32_ip_address:
            print(' [!] No Lightbrush server found!   ')
            print('     Make sure the Lightbrush tool is connected to the same WiFi.')
            sys.exit(1)
    else:
        esp32_ip_address = args.ip
        print(' [ ] Verifying Lightbrush server...\r', end='', flush=True)
        if not is_port_open(esp32_ip_address) or not is_lightbrush(esp32_ip_address):
            print(' [!] No Lightbrush server found!   ')
            print('     The specified IP address does not seem to be the lightbrush tool.')
            sys.exit(1)

    print(' [✓] Lightbrush server found: {}'.format(esp32_ip_address))

    session = requests.Session()
    session.get(f'http://{esp32_ip_address}/brightness?value={args.brightness}', verify=False)
    print(f' [✓] Set brightness to {args.brightness}')

    def robot_callback(value):
        r, g, b = [int(c * 255) for c in flat_data['colors'][value]]
        brightness = int(flat_data['gradients'][value] * 255)
        print(f', RGB: {r}, {g}, {b}, Brightness: {brightness}\r', end='', flush=True)
        session.get(f'http://{esp32_ip_address}/leds?rgb=[{r},{g},{b}]&brightness={brightness}', verify=False)

    asyncio.run(start_server(robot_callback))
