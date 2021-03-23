'''
Author: Riley Simpson
Description:
    LeagueHyper operates by taking a screenshot every second and attempting to locate an image.
    In it's current state, it only looks for penta kills. Altering the constant PENTA_REF to
    an image's file path relative to the current working directory will change the image
    pyautogui is locating. PENTA_MP3 contains the file path for the mp3/wav file to be played
    when PENTA_REF is located. Program is in the early stages, may mess around and all possible
    kill combinationes(double,triple, and quadra). Also, the audio sounds could be way cooler...
    If only it wasnt 3 AM on a Monday.
Modules:
    PythonAutoGUI: https://pyautogui.readthedocs.io/en/latest/index.html
    OpenCV: https://github.com/opencv/opencv-python (needed for the confidence keyword argument for pag)
    playsound: https://github.com/TaylorSMarks/playsound
    time:
'''
import pyautogui as pag
import playsound, time

PENTA_REF = 'pentakill.png'  # Image file to be located
PENTA_MP3 = 'woohoo.mp3'  # audio file to be played when ^^ is located

while True:
    print("Executed.")
    time.sleep(1)
    screen = pag.screenshot("images/currScreen.png")
    penta_img = pag.locateOnScreen('images/' + PENTA_REF, confidence=0.5)  # PIL image, None if not found
    if(penta_img):
        playsound.playsound(PENTA_MP3)
    else:
        print('Better luck next time, gamer.')