import os
import time

import Growl

from cli import CLI

class Main(object):
    def __init__(self, full_path_to_dir=None, command_to_execute=None):
        self.dir = full_path_to_dir
        self.command = command_to_execute

    def createDaemon(self):
    	# create - fork 1
    	try:
    		if os.fork() > 0: os._exit(0) # exit father...
    	except OSError, error:
    		CLI().error_and_exit('Fork #1 failed: %d (%s)' % (error.errno, error.strerror))

    	# it separates the son from the father
    	os.chdir('/')
    	os.setsid()
    	os.umask(0)

    	# create - fork 2
    	try:
    		pid = os.fork()
    		if pid > 0:
    		    CLI().info_and_exit('Daemon PID %d' % pid)
    	except OSError, error:
    		CLI.error_and_exit('fork #2 failed: %d (%s)' % (error.errno, error.strerror))

    	Ynspector(self.dir, self.command).run()
    	
class Ynspector(object):
    def __init__(self, dir=None, command=None):
        self.dir = dir
        self.command = command
    
    def run(self):
        DB = {}
        #img = Growl.Image.imageFromPath('./python-logo.gif')
        #growl = Growl.GrowlNotifier(applicationName='ynspector', applicationIcon=img, notifications=[''])
        growl = Growl.GrowlNotifier(applicationName='ynspector', applicationIcon=None, notifications=[''])
        growl.register()

        while True:
            changed = ''
        
            for root, dirs, files in os.walk(self.dir):
                for file in files:
                    if file.endswith('.py'):
                        full_file_name = '%s/%s' % (root, file)
                        stats = os.stat(full_file_name).st_mtime
                
                        if full_file_name not in DB:
                            changed = full_file_name
                
                        curr_stats = DB.get(full_file_name, 0)
                
                        if curr_stats != stats:
                            changed = full_file_name
                
                        DB[full_file_name] = stats
        
            ################################################        
            if changed != '':
                growl.notify('', 'File changed', changed)
            
                code = os.system("cd %s && %s" % (self.dir, self.command))
            
                if code == 0:
                    growl.notify('', 'Test Results', 'Tests passed!')
                else:
                    growl.notify('', 'Test Results', 'You dumb, there are failures in your tests.')
            
            time.sleep(2)