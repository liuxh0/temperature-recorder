'''
This program reads data produced by Arduino from the USB port and writes them
in a local file.
'''

import serial
from datetime import datetime
from time import sleep

input_buffer = b''
output_file = open('output.txt', 'w')


def main():
    global input_buffer

    arduino = serial.Serial('/dev/cu.usbmodem14201', 9600, timeout=.1)
    sleep(1)

    while True:
        if arduino.inWaiting() > 0:
            input_buffer += arduino.read_all()
            process_input_buffer()


def process_input_buffer():
    global input_buffer

    parts = input_buffer.split(b'\r\n')
    new_data = parts[:-1]
    input_buffer = parts[-1]

    for entry in new_data:
        line = str(datetime.now()) + ';' + entry.decode('utf-8')
        print(line)
        output_file.write(line + '\n')
        output_file.flush()


if __name__ == '__main__':
    main()
