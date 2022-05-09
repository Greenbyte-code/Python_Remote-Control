#https://www.youtube.com/watch?v=K1Ne_pGy2e8
import cv2
import numpy
import pyautogui
import keyboard

filename = "record"
screen_size = (1920, 1200)
codec = cv2.VideoWriter_fourcc(*"mp4v")
vid = cv2.VideoWriter(filename + ".mp4", codec, 20.0, (screen_size))

while True:
    img = pyautogui.screenshot()
    numpy_frame = numpy.array(img)
    frame = cv2.cvtColor(numpy_frame, cv2.COLOR_BGR2RGB)
    vid.write(frame)
    if keyboard.is_pressed("x"):

        break

cv2.destroyAllWindows()
vid.release()