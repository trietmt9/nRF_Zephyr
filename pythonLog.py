import serial 
import time 

ser = serial.Serial('/dev/ttyACM1', 115200)

while true: 
    data = ser.readline()
    print(data)
    f = open('log.txt', 'a')
    data = str(data)
    f.write(data)
    f.close()
    time.sleep(1)