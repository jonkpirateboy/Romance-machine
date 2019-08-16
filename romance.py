#coding=utf-8

#importera biblioteket for att prata med saker över gpio
import RPi.GPIO as GPIO
import time
import random
from pygame import mixer

#sätt gpio till rätt läge
GPIO.setmode(GPIO.BCM)

#sätt in vilka pins vad är kopplat
buttonPin = 23

#säg åt den pin som knappen är kopplad till att den ska lyssna på input
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#spin that wheel, dj
mixer.init()
dirtySongs = [
	'/home/pi/mp3/careless_whisper.mp3', 
	'/home/pi/mp3/i_want_to_know_what_love_is.mp3', 
	'/home/pi/mp3/cant_get_enough_of_your_love_babe.mp3', 
	'/home/pi/mp3/if_you_dont_know_me_by_now.mp3', 
	'/home/pi/mp3/say_you_say_me.mp3', 
	'/home/pi/mp3/sexual_healing.mp3'
]

#en loop som körs om och om igen och lyssnar på knapptryck
oldState = True
#i=0
while True:
  #hämta staten på knappen
  buttonState = GPIO.input(buttonPin)
  
  if buttonState != oldState:
    if buttonState == False:
        #sätt på musiken
        song = random.choice(dirtySongs)
        mixer.stop()
        mixer.music.load(song)
        mixer.music.play()
        time.sleep(1)
