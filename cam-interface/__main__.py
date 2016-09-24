import numpy
import cv2
import sys
from socketIO_client import SocketIO

server = sys.argv[1]

cam_num = int(sys.argv[2])

sensitivity = int(sys.argv[3])

img = None

was_left = False
was_action = False
was_right = False

def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)

def calculate_element(pos):
    global img
    global element_size
    average = 0
    counter = 0

    '''
    for x in range (element_size * pos,element_size * (pos +1)):
        for y in range (0,height):
            color = img[y][x]
            average += color
            counter += 1
    '''
    part = numpy.array_split(img, element_size,axis=1)[0]

    print(part)

    '''
    average /= counter

    average = average*average
    '''

    average = numpy.average(part)

    #print(average)

    if average > sensitivity:
        #cv2.rectangle(img, (element_size*pos, 0), (element_size*(pos + 1), height), (255, 255, 255), 50)
        return True

    return False

def to_socket(left,action,right):
    global was_left

    if was_left is not left:
        was_left = left
        if left is True:
            socketIO.emit('input', {'user': -1, 'key': 'left', 'state': 'down'})
        else:
            socketIO.emit('input', {'user': -1, 'key': 'left', 'state': 'up'})


cam = cv2.VideoCapture(cam_num)

width = int(cam.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))

element_size = int(width/3)

winName = "Movement Indicator"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)

# Read three images first:
t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)


socketIO = SocketIO(server, 3000)

while True:
    img = diffImg(t_minus, t, t_plus)

    #cv2.line(img, (element_size, 0), (element_size, int(height)), (255, 0, 0), 5)

    #cv2.line(img, (element_size*2, 0), (element_size*2, int(height)), (255, 0, 0), 5)

    left = calculate_element(0)

    #action = calculate_element(1)

    #right = calculate_element(2)

    cv2.imshow(winName, img)

    #to_socket(left,action,right)

    # Read next image
    t_minus = t_plus
    #t = t_plus
    t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyWindow(winName)
        break


