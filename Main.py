from playsound import playsound
from time import sleep, ctime
from random import randint

while True:
    playsound('Song.wav')
    print("hey that's pretty good! {}".format(ctime()))
    sleep(randint(10, 300))
