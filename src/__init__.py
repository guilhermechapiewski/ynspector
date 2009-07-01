from cli import CLI
from main import Main

version = "0.1.0"

def run():
    (options, args) = CLI().parse()

    if options.ynspector_version:
        msg = "ynspector v%s" % version
        CLI().info_and_exit(msg)

    # If CLI was correctly parsed, execute ynspector
    Main(options.full_path_to_dir, options.command_to_execute).createDaemon()