import serial
import time 
import re 
ser = serial.Serial('/dev/ttyACM1', 115200)
# 7-bit C1 ANSI sequences
ansi_escape = re.compile(r'''
    \x1B  # ESC
    (?:   # 7-bit C1 Fe (except CSI)
        [@-Z\\-_]
    |     # or [ for CSI, followed by a control sequence
        \[
        [0-?]*  # Parameter bytes
        [ -/]*  # Intermediate bytes
        [@-~]   # Final byte
    )
''', re.VERBOSE)

while True: 
    data = ser.readline().decode('utf-8', errors='ignore').strip()
    print(data)
    f = open('log.txt', 'a', encoding="utf-8")
    data = str(data)
    final_data = ansi_escape.sub('', data)
    f.write(final_data)
    f.close() 
    time.sleep(1)