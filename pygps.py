# Based on the Python GPS example given by SparkFun Electronics [A.Weiss]


import serial
from serial.tools import list_ports
from pynmea import nmea

# ===========  Global Variables   ===========
# =   Declare as 'global in the function    =
ser = 0

# ===========  Constants    ===========
BAUDRATE = 4800
COMPORT = 'COM3'

def scan():
    print([comport.device for comport in serial.tools.list_ports.comports()])


def init_serial():
    global ser
    ser = serial.Serial(
    port = COMPORT, 
    baudrate = BAUDRATE, 
    timeout =1
    )


def close_serial():
    ser.close()


        

def stream_serial():
    # stream data directly from the serial port
    while True:
        line = ser.readline()
        line_str = str(line)
        print(line_str)


def stream_position():
    # while True:
        for i in range(300):
            line = ser.readline()
            line_str = line.decode('utf8')
            # print(line_str)
            if(line_str[4] == 'G'):
                 print(line_str)
        





scan()
init_serial()
# stream_serial()
stream_position()
close_serial()
ser.close()
