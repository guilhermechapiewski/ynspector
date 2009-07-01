from optparse import OptionParser
import sys

class CLI(object):

    def __init__(self):
        self.__config_parser()

    def __config_parser(self):
        self.__parser = OptionParser()
        
        self.__parser.add_option('-c', '--command', 
                dest='command_to_execute', 
                default=None, 
                help='Command that ynspector should execute when a file is changed.')

        self.__parser.add_option('-d', '--dir', 
                dest='full_path_to_dir', 
                default=None, 
                help='Directory to inspect.')
                
        self.__parser.add_option('-v', '--version', 
                action='store_true',
                dest='ynspector_version', 
                default=False, 
                help='Displays ynspector's version and exit.')

    def get_parser(self):
        return self.__parser

    def parse(self):
        return self.__parser.parse_args()
        
    def error_and_exit(self, msg):
        self.msg('[ERROR] %s\n' % msg)
        sys.exit(1)

    def info_and_exit(self, msg):
        self.msg('%s\n' % msg)
        sys.exit(0)

    def msg(self, msg):
        print '%s' % msg