from urllib import urlretrieve
from getpass import getuser
from os import system
from time import time
from sha import sha
import os.path
from time import sleep

user = getuser()
#dir_path = 'Users/{}/Library/Applications/Desk-Stopper'.format(user)

if os.path.exists('/Users/{}/Desktop/ShowStopper'.format(user)) is False:
	command = 'mkdir "/Users/{}/Desktop/ShowStopper"'.format(user)
	system(command)


while True:
	try:
		name = sha(str(time())).hexdigest()
		print 'foo'
		urlretrieve('http://unsplash.it/1600/1600/?random', '/Users/{}/Desktop/ShowStopper/{}.jpeg'.format(user,name[:10]))
		system(''' osascript -e 'tell application "Finder" to set desktop picture to POSIX file "/Users/{}/Desktop/ShowStopper/{}.jpeg"' '''.format(user,name[:10]))
		sleep(7200) #wait two hours
	except Exception, e:
		print e
		sleep(300)
	


