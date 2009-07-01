import os
import sys
import time
import Growl
import subprocess


DIR = '/Users/gc/Projetos/python-guardian-osx'
USER_DIR = '/Users/gc/Projetos/vinagrette'

def run():
    DB = {}
    img = Growl.Image.imageFromPath('%s/python-logo.gif' % DIR)
    growl = Growl.GrowlNotifier(applicationName = 'python-guardian-osx', applicationIcon = img, notifications = [''])
    growl.register()

    while True:
        changed = ""
        
        for root, dirs, files in os.walk(USER_DIR):
            for file in files:
                if file.endswith(".py"):
                    full_file_name = "%s/%s" % (root, file)
                    stats = os.stat(full_file_name).st_mtime
                
                    if full_file_name not in DB:
                        changed = full_file_name
                
                    curr_stats = DB.get(full_file_name, 0)
                
                    if curr_stats != stats:
                        changed = full_file_name
                
                    DB[full_file_name] = stats
        
        ################################################        
        if changed != "":
            growl.notify('', 'File changed', changed)
            
            code = os.system("cd /Users/gc/Projetos/vinagrette/cma; ./manage.py test")
            
            if code == 0:
                growl.notify('', 'Test Results', 'Tests passed!')
            else:
                growl.notify('', 'Test Results', 'You dumb, there are failures in your tests.')
            
        time.sleep(2)

def createDaemon():
	# create - fork 1
	try:
		if os.fork() > 0: os._exit(0) # exit father...
	except OSError, error:
		print 'fork #1 failed: %d (%s)' % (error.errno, error.strerror)
		os._exit(1)

	# it separates the son from the father
	os.chdir('/')
	os.setsid()
	os.umask(0)

	# create - fork 2
	try:
		pid = os.fork()
		if pid > 0:
			print 'Daemon PID %d' % pid
			os._exit(0)
	except OSError, error:
		print 'fork #2 failed: %d (%s)' % (error.errno, error.strerror)
		os._exit(1)

	run()
		
if __name__ == '__main__':
    createDaemon()