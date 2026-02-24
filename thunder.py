import mpv 
import schedule 
from datetime import datetime, timedelta, time, tzinfo
import time
import os
import sys
import psutil
import logging

#Input your values into the 'changeme' section
starthrs = changeme
startmins = changeme
endhrs = changeme 
endmins = changeme

conthrs = 0; contmins = 00
now = datetime.now()
hrs = now.hour
mins = now.minute
start = (hrs >= starthrs and mins >= startmins)
cont = (hrs < endhrs  and mins >= contmins)
end = (hrs == endhrs and mins == endmins)
Player = mpv.MPV(video=False)

def reset_program():
	try:
		p= psutil.Process(os.getpid())
		for handler in p.get_open_files() + p.connections():
			os.close(handler.fd)
	except Exception as e:
		logging.error(e)

	python = sys.executable
	os.execl(python, python, *sys.argv)

def play_audio():
	now = datetime.now()
	print(f"Playing audio at {now}")
	Player.play('/home/jb/Documents/thunder/1sec.mp3')
	Player.wait_for_playback()
	checktime()

def checktime():
	now = datetime.now()
	hrs = now.hour
	mins = now.minute
	start = (hrs >= starthrs and mins == startmins)
	cont = (hrs < endhrs  and mins >= contmins)
	end = (hrs == endhrs  and mins == endmins)
	if  end == True:
		print(f"{now} is past {endhrs}:{endmins}, audio will resume at {starthrs}:{startmins}.")
		print("good morning")
	if cont == True:
		play_audio()
	if start == True:
		print('goodnight')
		play_audio()
	else:
		time.sleep(30)
		reset_program()
checktime()



