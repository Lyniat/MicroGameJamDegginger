import serial
import sys
from socketIO_client import SocketIO, LoggingNamespace

device = sys.argv[1]
server = sys.argv[2]

print ('connecting to '+ str(device))

MIN_ACTIVATION = 50

isActive = False

print ('trying to connect to server on: '+server)

def on_connect(*args):
    print('connected', args)
    socketIO.emit('register','player')

socketIO = SocketIO(server, 3000, LoggingNamespace)

# Listen
socketIO.on('connect', on_connect)

#socketIO.wait()

ser = serial.Serial(device, 9600)
while True:
    s = str(ser.readline())
    part_0 = s.split(':');

    if len(part_0) > 1:
        part_1 = part_0[1].split('\\');
        if len(part_1) > 1:
            result = part_1[0]
            print (result)
            num = int(result)

            if num is 0:
                continue

            if num >= MIN_ACTIVATION :
                print('touched');
                isActive = True
                socketIO.emit('input', {'user':-1, 'key':'right','state':'down'})
            else:
                isActive = False
                socketIO.emit('input', {'user': -1, 'key': 'right', 'state': 'up'})


