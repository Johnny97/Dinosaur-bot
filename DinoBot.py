from PIL import ImageGrab, ImageOps
from numpy import *
import pyautogui
import time


class Coordinates:
    replayBtn = (480, 468)
    dinosaur = (186, 500)


def restartgame():
    pyautogui.click(Coordinates.replayBtn)
    pyautogui.keyDown('down')


def pressspace():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    print("Jump")
    time.sleep(0.09)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')


def imageGrab():
    box = (Coordinates.dinosaur[0] + 60, Coordinates.dinosaur[1], Coordinates.dinosaur[0] + 150,
           Coordinates.dinosaur[1] + 5)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()


def main():
    restartgame()
    while True:
        if imageGrab() != 697:
            pressspace()
            time.sleep(0.01)


main()
