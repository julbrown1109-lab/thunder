import mpv 
import schedule 
from datetime import datetime, timedelta, time, tzinfo
import time
import os
import sys
import psutil
import logging

#Input your values into the 'changeme' section
endhrs = changeme
starthrs = changeme

#Definitions phase
#Defines the current time and the hours and minutes that need to be defined
now = datetime.now()
hrs = now.hour
mins = now.minute

#Defining what time the audio should start
start = hrs > starthrs 
end = hrs < endhrs 

#defining the times
timecheck = start or end
timestart = timecheck == True
timeend = timecheck == False

#for the mpv file
Player = mpv.MPV(video=False)

#Running the script 
def run(): 
	#Change the file path to your mp3
	Player.play('/your/path/to/audio.mp3')
	rest()

#Checking when the audio ends and replaying if still within the time
def rest():
	Player.wait_for_playback()
	if timestart:
		run()
	else: 
		restart_program()
#For the initial instance
def play_audio():
	print (f"playing audio at {now}")
	run()
def sleepytime():
	while timestart:
		now = datetime.now()
		play_audio()
#to run the script continuously
def restart_program():
	try: 
		p = psutil.Process(os.getpid())
		for handler in p.get_open_files() + p.connections():
			os.close(handler.fd)
	except Exception as e:
		logging.error(e)

	python = sys.executable
	os.execl(python, python, *sys.argv)

#Execution phase
if timestart:
	print("Have a good rest.")

while timeend:
	now = datetime.now()
	hrs = now.hour
	mins = now.minute
	print(f"not yet, its only {hrs}:{mins} wait until {starthrs}:00")
	time.sleep(60)
	restart_program()
else:
	sleepytime()

