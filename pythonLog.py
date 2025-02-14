import serial
import time 

ser = serial.Serial('/dev/ttyACM1', 115200)

while True: 
    data = ser.readline()
    print(data)
    f = open('log.txt', 'a', encoding="utf-8")
    data = str(data)
    f.write(data + "\n")
    f.close() 
    time.sleep(1)