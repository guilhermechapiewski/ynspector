from cli import CLI
from main import Main

version = "0.1.7"

def run():
    (options, args) = CLI().parse()

    if options.ynspector_version:
        msg = "ynspector v%s" % version
        CLI().info_and_exit(msg)

    if not options.full_path_to_dir or not options.command_to_execute:
        CLI().error_and_exit("You need to inform the path to inspect (-d) and the command to execute (-c)")

    # If CLI was correctly parsed, execute ynspector
    Main(options.full_path_to_dir, options.command_to_execute).createDaemon()