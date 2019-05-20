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
        
def stream_position_a():
    # while True:
        for i in range(300):
            line = ser.readline()
            line = line.decode('utf8')
            # print(line[4])
            if(line[4] == 'G'):
                gpgga = nmea.GPGGA()
                gpgga.parse(line)
                lats = gpgga.latitude
                longs = gpgga.longitude
                #convert degrees,decimal minutes to decimal degrees 
                lat1 = (float(lats[2]+lats[3]+lats[4]+lats[5]+lats[6]+lats[7]+lats[8]))/60
                lat_degrees = (float(lats[0]+lats[1])+lat1)
                long1 = (float(longs[3]+longs[4]+longs[5]+longs[6]+longs[7]+longs[8]+longs[9]))/60
                long_degrees = (float(longs[0]+longs[1]+longs[2])+long1)
                print(f"The latitude/longitude is {lat_degrees} -{long_degrees} ")
                print(line, end="")





scan()
init_serial()
# stream_serial()
# stream_position()
stream_position_a()
close_serial()
ser.close()
