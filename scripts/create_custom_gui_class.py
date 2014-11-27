__author__ = 'chris.maue'


#######################################################################################################################
# Import required libraries
#######################################################################################################################
import guicodebuilder
import logging
import os
import sys


#######################################################################################################################
# Determine project path and auto-set debug log file and gui configuration file names as appropriate
#######################################################################################################################
projectPath = os.path.split(sys.argv[0])
debugLogFile = os.path.normcase(os.path.join(projectPath[0], 'debug.log'))
guiIniFile = os.path.normcase(os.path.join(projectPath[0], 'autofilename_gui_setup.ini'))


#######################################################################################################################
# Start program logger / debugger
#######################################################################################################################
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    filename=debugLogFile,
                    filemode='w')
logging.info('[Main] Program Logger Started')
logging.info('[Main] Logging to file: %s' % debugLogFile)
logging.info('[Main] Using GUI configuration file: %s' % guiIniFile)


#######################################################################################################################
# Start application window (runs in main thread)
#######################################################################################################################
gui_object = guicodebuilder.gui(guiIniFile, debugLogFile)
gui_object.create_class()