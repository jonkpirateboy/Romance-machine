#coding=utf-8

#Import librarys
import RPi.GPIO as GPIO
import time
import random
from pygame import mixer

#Set GPIO
GPIO.setmode(GPIO.BCM)

#Set pin to use
buttonPin = 23

#Listen for button press
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Use mixer
mixer.init()

#Put songs in array
dirtySongs = [
	'/home/pi/mp3/careless_whisper.mp3', 
	'/home/pi/mp3/i_want_to_know_what_love_is.mp3', 
	'/home/pi/mp3/cant_get_enough_of_your_love_babe.mp3', 
	'/home/pi/mp3/if_you_dont_know_me_by_now.mp3', 
	'/home/pi/mp3/say_you_say_me.mp3', 
	'/home/pi/mp3/sexual_healing.mp3'
]

#Set state of button
oldState = True

#loop button state
while True:
  #Get button state
  buttonState = GPIO.input(buttonPin)
  
  if buttonState != oldState:
    if buttonState == False:
      #Choose song
      song = random.choice(dirtySongs)
      #Play the song if no song is playing
      if mixer.music.get_busy() == False:
        mixer.music.load(song)
        mixer.music.play()
        time.sleep(1)
      #If a song is playing, stop it
      else:
        mixer.music.stop()
        time.sleep(1)
