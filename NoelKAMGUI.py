import pyautogui
import time
import threading from Thread

'''       
print('press Ctrl-C to quit.')
# TODO: Get and print the mouse coordinatesself.

try:
    while True:
        #TODO: Get and print the mouse coordinates
        x, y = pyautogui.position()
        positionStr = 'X:' + str(x).rjust(4) + 'Y:' + str(y).rjust(4)
        print(positionStr)
        time.sleep(1)
except KeyboardInterrupt:
    print('\nDone.')
'''

while True:
    pyautogui.typewrite(' space')
    time.sleep(0.25)
    pyautogui.keyDown('left')
    time.sleep(0.63)
    pyautogui.keyUp('left')


def randomly_move_left():
    time.sleep(2)
    pyautogui,keyDown('left')
    pyautogui.keyUp('left')

def randomly_move_right():
    while True:
        time.sleep(2)
        pyautogui.keyDown('right')
        pyautogui.keyUp('right')

def fire():
    while True:
        pyautogui.typewrite([' space'])
        time.sleep(0.25)


go_left_thread = Threading(target=randomly_move_left)
go_left_thread.start()
go_right_thread = Thread(target=randomly_move_right)
go_right_thread.start()
fire_thread = Thread(target=fire)
fire_thread.start()
