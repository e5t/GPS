import serial 

# ser = 0 

# def init_serial():
#     print('Found Ports:')
#     for n,s in scan():
#         print(s)
#     print(' ')


def scan():
    # available = []
    for i in range(256):
        try:
            s = serial.Serial("COM4")
            #available.append((i, s.name))
            print(s.name)
            s.close()
        except serial.SerialException:
            pass
    return available

#vinit_serial()
scan()

