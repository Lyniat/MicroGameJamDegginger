import serial
import sys
from socketIO_client import SocketIO
import re

timing_pattern = re.compile('T\ ([0-9]*):\ ([0-9]*)')

server = sys.argv[2]

device = sys.argv[1]

print ('connecting to '+ str(device))

ring_0=[705]*5000
ring_1=[780]*5000
ring_2=[820]*5000


MIN_ACTIVATION_0 = 705
MIN_ACTIVATION_1 = 780
MIN_ACTIVATION_2 = 820

trigger_level = 25

isActive_0 = False
isActive_1 = False
isActive_2 = False



print ('trying to connect to server on: '+server)

def on_connect(self):
    print('connected')
    socketIO.emit('register','player')

socketIO = SocketIO(server, 3000)

#socketIO.wait()

ser = serial.Serial(device, 115200)

while True:
    s = ser.readline()

    test = s.decode('ascii')
    reparts = timing_pattern.match(test)


    if(reparts):

        device_num = int(reparts.groups()[0])
        value = int(reparts.groups()[1])

        #print(device_num)

        if device_num is 0:
            print(MIN_ACTIVATION_0)

            if not isActive_0:
                ring_0.append(value)
                ring_0.__delitem__(0)
                MIN_ACTIVATION_0 = int(sum(ring_0)/len(ring_0))+trigger_level

            if value >= MIN_ACTIVATION_0:
                if not isActive_0:
                    print('touched');
                    isActive_0 = True
                    socketIO.emit('input', {'user': -1, 'key': 'left', 'state': 'down'})
            else:
                if isActive_0:
                    print('released');
                    isActive_0 = False
                    socketIO.emit('input', {'user': -1, 'key': 'left', 'state': 'up'})

        if device_num is 1:

            print(MIN_ACTIVATION_1)

            if not isActive_1:
                ring_1.append(value)
                ring_1.__delitem__(0)
                MIN_ACTIVATION_1 = int(sum(ring_1)/len(ring_1))+trigger_level
            if value >= MIN_ACTIVATION_1:
                if not isActive_1:
                    print('touched');
                    isActive_1 = True
                    socketIO.emit('input', {'user': -1, 'key': 'right', 'state': 'down'})
            else:
                if isActive_1:
                    print('released');
                    isActive_1 = False
                    socketIO.emit('input', {'user': -1, 'key': 'right', 'state': 'up'})

        if device_num is 2:

            print(MIN_ACTIVATION_2)
            if not isActive_2:
                ring_2.append(value)
                ring_2.__delitem__(0)
                MIN_ACTIVATION_2 = int(sum(ring_2)/len(ring_2))+trigger_level
            if value >= MIN_ACTIVATION_2:
                if not isActive_2:
                    print('touched');
                    isActive_2 = True
                    socketIO.emit('input', {'user': -1, 'key': 'action', 'state': 'down'})
            else:
                if isActive_2:
                    print('released');
                    isActive_2 = False
                    socketIO.emit('input', {'user': -1, 'key': 'action', 'state': 'up'})


