# Romance machine
Code and build instructions for [Romance machine](https://www.reddit.com/r/raspberry_pi/comments/cowqrg/romance_machine_to_be_pressed_instead_of_saying/)

Install [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) on a Raspberry Pi

Buy a [button](https://www.kjell.com/se/produkter/el-verktyg/elektronik/elektromekanik/strombrytare/tryckstrombrytare/strombrytare-1-pol-fran-(till)-rod-p36011?fbclid=IwAR0jVSrSGsIbbd9ozXCtYwZDZijL6pdAcMhqYPt5dp17MCO4nXWOHzEONdA) and [jumper wires](https://www.kjell.com/se/produkter/el-verktyg/utvecklingskit/arduino/tillbehor/luxorparts-delbar-kopplingskabel-40-pol-hane-hona-p87900)

Connect two wires to pins 5 and 23, and to your button

Open console and enter
```
pip install pygame
```

Download [the script](romance.py) and put it in your home folder, /home/pi/

You'll need to change the list of songs to songs that you have on your Pi.

Open console and enter
```
sudo nano /etc/rc.local
```
In /etc/rc.local you enter 
```
python /home/pi/romance.py
```
before exit 0, that will make the script run on startup

Restart your Pi and press the button.