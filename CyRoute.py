import threading
from FlaskWebserver import startWebserver
from argparse import ArgumentParser
from pyfiglet import Figlet
from pyFiles import config, databaseHandler
from pyFiles.commandHandler import Handler

custom_fig = Figlet(font='doom')
print(custom_fig.renderText('CyRoute'))

parser = ArgumentParser()
parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")
parser.add_argument("-sts", "--startserver", help="Debug: Start Flask Server", action="store_true")
parser.add_argument("-bsql", "--buildSql", help="Debug: Build Database", action="store_true")
parser.add_argument("-u", "--url", dest="url", help="used to set URL to clone",
                    type=int)
parser.add_argument("-p", "--port", help="Define the Webserver port (80 on default)",
                    type=int)
parser.add_argument("-st", "--start", help="Starts the tool", action="store_true")
args = parser.parse_args()

if args.verbosity:
    config.verbose = True
    print("Verbosity on!")

if args.buildSql:
    databaseHandler.create_connection("CyRoute.db")

if args.port:
    config.port = args.port
    if config.verbose:
        print("VERBOSE: Port set to {}").format(args.port)

if args.startserver:
    config.serverIsUp = True
    threading.Thread(target=startWebserver).start()

threading.Thread(target=Handler()).start()

