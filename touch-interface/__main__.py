import serial
import sys
from socketIO_client import SocketIO


server = sys.argv[2]

device = sys.argv[1]

print ('connecting to '+ str(device))

MIN_ACTIVATION = 50

isActive = False

print ('trying to connect to server on: '+server)

def on_connect(self):
    print('connected')
    socketIO.emit('register','player')

socketIO = SocketIO(server, 3000)

#socketIO.wait()

ser = serial.Serial(device, 9600)
while True:
    s = str(ser.readline())
    part_0 = s.split(':');

    if len(part_0) > 1:
        part_1 = part_0[1].split('\\');
        if len(part_1) > 1:
            result = part_1[0]
            #print (result)
            num = int(result)

            if num is 0:
                continue

            if num >= MIN_ACTIVATION :
                if not isActive:
                    print('touched');
                    isActive = True
                    socketIO.emit('input', {'user':-1, 'key':'right','state':'down'})
            else:
                if isActive:
                    print('released');
                    isActive = False
                    socketIO.emit('input', {'user': -1, 'key': 'right', 'state': 'up'})


