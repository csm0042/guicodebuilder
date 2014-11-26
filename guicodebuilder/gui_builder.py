import logging
from .gui_callbacks import *
import os
import tkinter as tk
import configparser


#######################################################################################################################
# Define Helper functions
#######################################################################################################################
def CountWidgetByType(iniFile, searchString):
    import configparser
    Config = configparser.ConfigParser()
    Config.read(iniFile)

    # Initialize counter
    Count = 0

    # Count each of the various types of entries in the INI file
    for section in Config.sections():
        foundPointer = section.find(searchString)
        if foundPointer != -1:
            Count = Count + 1
        pass
    pass
    # Return results
    return Count


#######################################################################################################################
# Define Window class
#######################################################################################################################
class Window(object):
    def __init__(self):
        self.width = str()
        self.height = str()
        self.posX = str()
        self.posY = str()
        self.title = str()
        self.backgroundColor = str()
        self.iniFile = str()
        self.section = str()
        self.junk = str()


#######################################################################################################################
# Define Frame widget class
#######################################################################################################################
class Frame(object):
    def __init__(self):
        self.backgroundColor = str()
        self.borderwidth = str()
        self.colormap = str()
        self.container = str()
        self.cursor = str()
        self.height = str()
        self.highlightBackgroundColor = str()
        self.highlightColor = str()
        self.highlightThickness = str()
        self.padX = str()
        self.padY = str()
        self.relief = str()
        self.takeFocus = str()
        self.visual = str()
        self.width = str()
        self.iniFile = str()
        self.section = str()


#######################################################################################################################
# Define Message widget class
#######################################################################################################################
class Message(object):
    def __init__(self):
        self.anchor = str()
        self.aspect = str()
        self.backgroundColor = str()
        self.borderwidth = str()
        self.cursor = str()
        self.font = str()
        self.fontSize = str()
        self.foregroundColor = str()
        self.highlightBackground = str()
        self.highlightBackgroundColor = str()
        self.highlightThickness = str()
        self.justify = str()
        self.padX = str()
        self.padY = str()
        self.relief = str()
        self.takeFocus = str()
        self.text = str()
        self.textVariable = str()
        self.width = str()
        self.iniFile = str()
        self.section = str()


#######################################################################################################################
# Define Text widget class
#######################################################################################################################
class Text(object):
    def __init__(self):
        self.autoSeparators = str()
        self.backgroundColor = str()
        self.backgroundStipple = str()
        self.borderwidth = str()
        self.cursor = str()
        self.exportSelection = str()
        self.font = str()
        self.fontSize = str()
        self.foregroundColor = str()
        self.foregroundStipple = str()
        self.height = str()
        self.highlightBackgroundColor = str()
        self.highlightColor = str()
        self.highlightThickness = str()
        self.insertBackground = str()
        self.insertBorderwidth = str()
        self.insertOffTime = str()
        self.insertOnTime = str()
        self.insertWidth = str()
        self.justify = str()
        self.lmargin1 = str()
        self.lmargin2 = str()
        self.maxUndo = str()
        self.padX = str()
        self.padY = str()
        self.offset = str()
        self.overstrike = str()
        self.relief = str()
        self.rmargin = str()
        self.selectBackgroundColor = str()
        self.selectForegroundColor = str()
        self.selectBorderwidth = str()
        self.setGrid = str()
        self.spacing1 = str()
        self.spacing2 = str()
        self.spacing3 = str()
        self.state = str()
        self.tabs = str()
        self.takeFocus = str()
        self.text = str()
        self.underline = str()
        self.undo = str()
        self.width = str()
        self.wrap = str()
        self.xScrollCommand = str()
        self.yScrollCommand = str()
        self.iniFile = str()
        self.section = str()


#######################################################################################################################
# Define Button widget class
#######################################################################################################################
class Button(object):
    def __init__(self):
        self.activeBackgroundColor = str()
        self.activeForegroundColor = str()
        self.anchor = str()
        self.backgroundColor = str()
        self.bitmap = str()
        self.borderwidth = int()
        self.command = int()
        self.compound = str()
        self.cursor = str()
        self.default = str()
        self.disableForeground = str()
        self.font = str()
        self.fontSize = int()
        self.foregroundColor = str()
        self.height = int()
        self.highlightBackgroundColor = str()
        self.highlightColor = str()
        self.highlightThickness = int()
        self.image = str()
        self.justify = str()
        self.overRelief = str()
        self.padX = int()
        self.padY = int()
        self.relief = str()
        self.repeatDelay = int()
        self.repeatInterval = int()
        self.state = str()
        self.takeFocus = str()
        self.text = str()
        self.textVariable = str()
        self.underline = str()
        self.width = int()
        self.wrapLength = int()
        self.iniFile = str()
        self.section = str()


#######################################################################################################################
# Define place settings class
#######################################################################################################################
class Place(object):
    def __init__(self):
        self.anchor = str()
        self.borderMode = str()
        self.height = str()
        self.width = str()
        self.relHeight = str()
        self.relWidth = str()
        self.relX = str()
        self.relY = str()
        self.offsetX = str()
        self.offsetY = str()
        self.iniFile = str()
        self.section = str()


#######################################################################################################################
# Define GUI class
#######################################################################################################################
class gui(object):
    def __init__(self, inifile, logfile):
        self.inifile = inifile
        self.logfile = logfile
        self.codelines = []
        self.field = int()
        self.address = int()
        self.text_to_write = str()
        self.text_to_write_mem = str()
        self.place_settings = Place()
        self.path = str()
        self.codetowritetofile = str()

        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s',
                            filename=self.logfile, filemode='w')
        logging.info('[gui.__init__] Appwindow object created')

        self.root = tk.Tk()
        self.section = str()
        self.Window = Window()

        self.frameCount = CountWidgetByType(self.inifile, "frame")
        self.Frame = Frame()
        self.FramePlace = Place()
        self.tkFrame = [tk.Frame() for i in range(self.frameCount)]
        logging.info('[gui.__init__] Found configuration data for %d "frame" widgets' %self.frameCount)

        self.messageCount = CountWidgetByType(self.inifile, "message")
        self.Message = Message()
        self.MessagePlace = Place()
        self.tkMessage = [tk.Message() for i in range(self.messageCount)]
        logging.info('[gui.__init__] Found configuration data for %d "message" widgets' %self.messageCount)

        self.textCount = CountWidgetByType(self.inifile, "text")
        self.Text = Text()
        self.TextPlace = Place()
        self.tkText = [tk.Text() for i in range(self.textCount)]
        self.tkTextHandshake = [str() for i in range(self.textCount)]
        logging.info('[gui.__init__] Found configuration data for %d "text" widgets' %self.textCount)

        self.buttonCount = CountWidgetByType(self.inifile, "button")
        self.Button = Button()
        self.ButtonPlace = Place()
        self.tkButton = [tk.Button() for i in range(self.buttonCount)]
        self.ButtonInput = [bool() for i in range(self.buttonCount)]
        logging.info('[gui.__init__] Found configuration data for %d "button" widgets' %self.buttonCount)



    def create_class(self):

        ################################################################################################################
        # BEGIN SCRIPT BY IMPORTING DEPENDENCIES
        ################################################################################################################
        self.codelines.append('\n################################################################################################################')
        self.codelines.append('\n#IMPORT LIBRARIES')
        self.codelines.append('\n################################################################################################################')
        self.codelines.append('\nimport logging')
        self.codelines.append('\nimport tkinter as tk')
        self.codelines.append('\n')
        self.codelines.append('\n')


        ################################################################################################################
        # DEFINE HELPER CLASSES AND MODULES
        ################################################################################################################
        self.codelines.append('\n################################################################################################################')
        self.codelines.append('\n#DEFINE CLASS')
        self.codelines.append('\n################################################################################################################')
        self.codelines.append('\nclass Window(object):')
        self.codelines.append('\n\tdef __init__(self):')
        self.codelines.append('\n\t\tself.width = str()')
        self.codelines.append('\n\t\tself.height = str()')
        self.codelines.append('\n\t\tself.posX = str()')
        self.codelines.append('\n\t\tself.posY = str()')
        self.codelines.append('\n\t\tself.title = str()')
        self.codelines.append('\n\t\tself.backgroundColor = str()')
        self.codelines.append('\n\t\tself.title = str()')
        self.codelines.append('\n')
        self.codelines.append('\n')
        self.codelines.append('\nclass Frame(object):')
        self.codelines.append('\n\tdef __init__(self):')
        self.codelines.append('\n\t\tself.backgroundColor = str()')
        self.codelines.append('\n\t\tself.borderwidth = str()')
        self.codelines.append('\n\t\tself.colormap = str()')
        self.codelines.append('\n\t\tself.container = str()')
        self.codelines.append('\n\t\tself.cursor = str()')
        self.codelines.append('\n\t\tself.height = str()')
        self.codelines.append('\n\t\tself.highlightBackgroundColor = str()')
        self.codelines.append('\n\t\tself.highlightColor = str()')
        self.codelines.append('\n\t\tself.highlightThickness = str()')
        self.codelines.append('\n\t\tself.padX = str()')
        self.codelines.append('\n\t\tself.padY = str()')
        self.codelines.append('\n\t\tself.relief = str()')
        self.codelines.append('\n\t\tself.takeFocus = str()')
        self.codelines.append('\n\t\tself.visual = str()')
        self.codelines.append('\n\t\tself.width = str()')
        self.codelines.append('\n')
        self.codelines.append('\n')
        self.codelines.append('\nclass Message(object):')
        self.codelines.append('\n\tdef __init__(self):')
        self.codelines.append('\n\t\tself.anchor = str()')
        self.codelines.append('\n\t\tself.anchor = str()')
        self.codelines.append('\n\t\tself.aspect = str()')
        self.codelines.append('\n\t\tself.backgroundColor = str()')
        self.codelines.append('\n\t\tself.borderwidth = str()')
        self.codelines.append('\n\t\tself.cursor = str()')
        self.codelines.append('\n\t\tself.font = str()')
        self.codelines.append('\n\t\tself.fontSize = str()')
        self.codelines.append('\n\t\tself.foregroundColor = str()')
        self.codelines.append('\n\t\tself.highlightBackground = str()')
        self.codelines.append('\n\t\tself.highlightBackgroundColor = str()')
        self.codelines.append('\n\t\tself.highlightThickness = str()')
        self.codelines.append('\n\t\tself.justify = str()')
        self.codelines.append('\n\t\tself.padX = str()')
        self.codelines.append('\n\t\tself.padY = str()')
        self.codelines.append('\n\t\tself.relief = str()')
        self.codelines.append('\n\t\tself.takeFocus = str()')
        self.codelines.append('\n\t\tself.text = str()')
        self.codelines.append('\n\t\tself.textVariable = str()')
        self.codelines.append('\n\t\tself.width = str()')
        self.codelines.append('\n')
        self.codelines.append('\n')
        self.codelines.append('\nclass Text(object):')
        self.codelines.append('\n\tdef __init__(self):')
        self.codelines.append('\n\t\tself.autoSeparators = str()')
        self.codelines.append('\n\t\tself.backgroundColor = str()')
        self.codelines.append('\n\t\tself.backgroundStipple = str()')
        self.codelines.append('\n\t\tself.borderwidth = str()')
        self.codelines.append('\n\t\tself.cursor = str()')
        self.codelines.append('\n\t\tself.exportSelection = str()')
        self.codelines.append('\n\t\tself.font = str()')
        self.codelines.append('\n\t\tself.fontSize = str()')
        self.codelines.append('\n\t\tself.foregroundColor = str()')
        self.codelines.append('\n\t\tself.foregroundStipple = str()')
        self.codelines.append('\n\t\tself.height = str()')
        self.codelines.append('\n\t\tself.highlightBackgroundColor = str()')
        self.codelines.append('\n\t\tself.highlightColor = str()')
        self.codelines.append('\n\t\tself.highlightThickness = str()')
        self.codelines.append('\n\t\tself.insertBackground = str()')
        self.codelines.append('\n\t\tself.insertBorderwidth = str()')
        self.codelines.append('\n\t\tself.insertOffTime = str()')
        self.codelines.append('\n\t\tself.insertOnTime = str()')
        self.codelines.append('\n\t\tself.insertWidth = str()')
        self.codelines.append('\n\t\tself.justify = str()')
        self.codelines.append('\n\t\tself.lmargin1 = str()')
        self.codelines.append('\n\t\tself.lmargin2 = str()')
        self.codelines.append('\n\t\tself.maxUndo = str()')
        self.codelines.append('\n\t\tself.padX = str()')
        self.codelines.append('\n\t\tself.padY = str()')
        self.codelines.append('\n\t\tself.offset = str()')
        self.codelines.append('\n\t\tself.overstrike = str()')
        self.codelines.append('\n\t\tself.relief = str()')
        self.codelines.append('\n\t\tself.rmargin = str()')
        self.codelines.append('\n\t\tself.selectBackgroundColor = str()')
        self.codelines.append('\n\t\tself.selectForegroundColor = str()')
        self.codelines.append('\n\t\tself.selectBorderwidth = str()')
        self.codelines.append('\n\t\tself.setGrid = str()')
        self.codelines.append('\n\t\tself.spacing1 = str()')
        self.codelines.append('\n\t\tself.spacing2 = str()')
        self.codelines.append('\n\t\tself.spacing3 = str()')
        self.codelines.append('\n\t\tself.state = str()')
        self.codelines.append('\n\t\tself.tabs = str()')
        self.codelines.append('\n\t\tself.takeFocus = str()')
        self.codelines.append('\n\t\tself.text = str()')
        self.codelines.append('\n\t\tself.underline = str()')
        self.codelines.append('\n\t\tself.undo = str()')
        self.codelines.append('\n\t\tself.width = str()')
        self.codelines.append('\n\t\tself.wrap = str()')
        self.codelines.append('\n\t\tself.xScrollCommand = str()')
        self.codelines.append('\n\t\tself.yScrollCommand = str()')
        self.codelines.append('\n')
        self.codelines.append('\n')
        self.codelines.append('\nclass Button(object):')
        self.codelines.append('\n\tdef __init__(self):')
        self.codelines.append('\n\t\tself.activeBackgroundColor = str()')
        self.codelines.append('\n\t\tself.activeForegroundColor = str()')
        self.codelines.append('\n\t\tself.anchor = str()')
        self.codelines.append('\n\t\tself.backgroundColor = str()')
        self.codelines.append('\n\t\tself.bitmap = str()')
        self.codelines.append('\n\t\tself.borderwidth = str()')
        self.codelines.append('\n\t\tself.command = str()')
        self.codelines.append('\n\t\tself.compound = str()')
        self.codelines.append('\n\t\tself.cursor = str()')
        self.codelines.append('\n\t\tself.default = str()')
        self.codelines.append('\n\t\tself.disableForeground = str()')
        self.codelines.append('\n\t\tself.font = str()')
        self.codelines.append('\n\t\tself.fontSize = str()')
        self.codelines.append('\n\t\tself.foregroundColor = str()')
        self.codelines.append('\n\t\tself.height = str()')
        self.codelines.append('\n\t\tself.highlightBackgroundColor = str()')
        self.codelines.append('\n\t\tself.highlightColor = str()')
        self.codelines.append('\n\t\tself.highlightThickness = str()')
        self.codelines.append('\n\t\tself.image = str()')
        self.codelines.append('\n\t\tself.justify = str()')
        self.codelines.append('\n\t\tself.overRelief = str()')
        self.codelines.append('\n\t\tself.padX = str()')
        self.codelines.append('\n\t\tself.padY = str()')
        self.codelines.append('\n\t\tself.relief = str()')
        self.codelines.append('\n\t\tself.repeatDelay = str()')
        self.codelines.append('\n\t\tself.repeatInterval = str()')
        self.codelines.append('\n\t\tself.state = str()')
        self.codelines.append('\n\t\tself.takeFocus = str()')
        self.codelines.append('\n\t\tself.text = str()')
        self.codelines.append('\n\t\tself.textVariable = str()')
        self.codelines.append('\n\t\tself.underline = str()')
        self.codelines.append('\n\t\tself.width = str()')
        self.codelines.append('\n\t\tself.wrapLength = str()')
        self.codelines.append('\n')
        self.codelines.append('\n')
        self.codelines.append('\nclass Place(object):')
        self.codelines.append('\n\tdef __init__(self):')
        self.codelines.append('\n\t\tself.anchor = str()')
        self.codelines.append('\n\t\tself.borderMode = str()')
        self.codelines.append('\n\t\tself.height = str()')
        self.codelines.append('\n\t\tself.width = str()')
        self.codelines.append('\n\t\tself.relHeight = str()')
        self.codelines.append('\n\t\tself.relWidth = str()')
        self.codelines.append('\n\t\tself.relX = str()')
        self.codelines.append('\n\t\tself.relY = str()')
        self.codelines.append('\n\t\tself.offsetX = str()')
        self.codelines.append('\n\t\tself.offsetY = str()')
        self.codelines.append('\n')
        self.codelines.append('\n')







        ################################################################################################################
        # DEFINE GUI CLASS AND ADD __init__ METHOD
        ################################################################################################################
        self.codelines.append('\n################################################################################################################')
        self.codelines.append('\n#DEFINE GUI CLASS')
        self.codelines.append('\n################################################################################################################')
        self.codelines.append('\nclass gui(object):')
        self.codelines.append('\n\tdef __init__(self, logfile):')
        self.codelines.append('\n\t\tself.logfile = logfile')
        self.codelines.append('\n\t\tself.root = tk.Tk()')
        self.codelines.append('\n')
        self.codelines.append('\n\t\tlogging.basicConfig(level=logging.DEBUG, ')
        self.codelines.append('''\n\t\t\tformat='%(asctime)s %(levelname)-8s %(message)s', ''')
        self.codelines.append('''\n\t\t\tfilename=self.logfile, filemode='w')''')
        self.codelines.append('''\n\t\tlogging.info('[gui.__init__] Appwindow object created')''')
        self.codelines.append('\n')
        self.codelines.append('\n\t\tself.frameCount = ')
        self.codelines.append(str(CountWidgetByType(self.inifile, "frame")))
        self.codelines.append('\n\t\tself.Frame = Frame()')
        self.codelines.append('\n\t\tself.frame_settings = Frame()')
        self.codelines.append('\n\t\tself.FramePlace = Place()')
        self.codelines.append('\n\t\tself.tkFrame = [tk.Frame() for i in range(self.frameCount)]')
        self.codelines.append("\n\t\tlogging.info('[gui.__init__] Found configuration data for %d frame widgets' % self.frameCount)")
        self.codelines.append('\n')
        self.codelines.append('\n\t\tself.messageCount = ')
        self.codelines.append(str(CountWidgetByType(self.inifile, "message")))
        self.codelines.append('\n\t\tself.Message = Message()')
        self.codelines.append('\n\t\tself.message_settings = Message()')
        self.codelines.append('\n\t\tself.MessagePlace = Place()')
        self.codelines.append('\n\t\tself.tkMessage = [tk.Message() for i in range(self.messageCount)]')
        self.codelines.append("\n\t\tlogging.info('[gui.__init__] Found configuration data for %d message widgets' % self.messageCount)")
        self.codelines.append('\n')
        self.codelines.append('\n\t\tself.textCount = ')
        self.codelines.append(str(CountWidgetByType(self.inifile, "text")))
        self.codelines.append('\n\t\tself.Text = Text()')
        self.codelines.append('\n\t\tself.text_settings = Text()')
        self.codelines.append('\n\t\tself.TextPlace = Place()')
        self.codelines.append('\n\t\tself.tkText = [tk.Text() for i in range(self.textCount)]')
        self.codelines.append("\n\t\tlogging.info('[gui.__init__] Found configuration data for %d text widgets' % self.textCount)")
        self.codelines.append('\n')
        self.codelines.append('\n\t\tself.buttonCount = ')
        self.codelines.append(str(CountWidgetByType(self.inifile, "button")))
        self.codelines.append('\n\t\tself.Button = Button()')
        self.codelines.append('\n\t\tself.button_settings = Button()')
        self.codelines.append('\n\t\tself.ButtonPlace = Place()')
        self.codelines.append('\n\t\tself.tkButton = [tk.Button() for i in range(self.buttonCount)]')
        self.codelines.append('\n\t\tself.ButtonInput = [bool() for i in range(self.buttonCount)]')
        self.codelines.append("\n\t\tlogging.info('[gui.__init__] Found configuration data for %d button widgets' % self.buttonCount)")
        self.codelines.append('\n')
        self.codelines.append('\n')



        ################################################################################################################
        # CREATE TKINTER MAIN WINDOW
        ################################################################################################################
        self.Window.section = "main window"

        Config = configparser.ConfigParser()
        Config.read(self.inifile)
        dict1 = {}
        options = Config.options(self.Window.section)
        for option in options:
            try:
                dict1[option] = Config.get(self.Window.section, option)
                if dict1[option] == -1:
                    pass
            except:
                dict1[option] = None

        self.Window.width = dict1['width']
        self.Window.height = dict1['height']
        self.Window.posX = dict1['pos x']
        self.Window.posY = dict1['pos y']
        self.Window.title = dict1['title']
        self.Window.backgroundColor = dict1['background color']

        self.codelines.append('\n\t################################################################################################################')
        self.codelines.append('\n\t#CREATE TKINTER MAIN WINDOW')
        self.codelines.append('\n\t################################################################################################################')
        self.codelines.append('\n\tdef create_window(self):')
        self.codelines.append('''\n\t\tlogging.info('[gui.create_window] Adjusting window geometry')''')

        self.codelines.append('''\n\t\tself.root.geometry("%sx%s+%s+%s" % (''')
        self.codelines.append(self.Window.width)
        self.codelines.append(', ')
        self.codelines.append(self.Window.height)
        self.codelines.append(', ')
        self.codelines.append(self.Window.posX)
        self.codelines.append(', ')
        self.codelines.append(self.Window.posY)
        self.codelines.append('))')

        if self.Window.backgroundColor != "":
            self.codelines.append("\n\t\tself.root.config(background='")
            self.codelines.append(self.Window.backgroundColor)
            self.codelines.append("')")
            self.codelines.append('''\n\t\tlogging.info('[gui.create_window] Adjusting window background color')''')

        if self.Window.title != '':
            self.codelines.append("\n\t\tself.root.title('")
            self.codelines.append(self.Window.title)
            self.codelines.append("')")
            self.codelines.append('''\n\t\tlogging.info('[gui.create_window] Setting window title')''')

        self.codelines.append('\n')


        ################################################################################################################
        # CALL LOOP TO CREATE FRAME WIDGETS
        ################################################################################################################
        self.codelines.append("\n\t\tlogging.info('[gui.create_window] Starting frame widget loop')")
        for i in range(0, self.frameCount):
            self.Frame.section = str("frame" + str(i+1))

            Config = configparser.ConfigParser()
            Config.read(self.inifile)
            dict1 = {}
            options = Config.options(self.Frame.section)
            for option in options:
                try:
                    dict1[option] = Config.get(self.Frame.section, option)
                    if dict1[option] == -1:
                        pass
                except:
                    dict1[option] = None

            self.Frame.backgroundColor = dict1['background color']
            self.Frame.borderWidth = dict1['border width']
            self.Frame.colormap = dict1['color map']
            self.Frame.container = dict1['container']
            self.Frame.cursor = dict1['cursor']
            self.Frame.height = dict1['height']
            self.Frame.highlightBackgroundColor = dict1['highlight background color']
            self.Frame.highlightColor = dict1['highlight color']
            self.Frame.highlightThickness = dict1['highlight thickness']
            self.Frame.padX = dict1['pad x']
            self.Frame.padY = dict1['pad y']
            self.Frame.relief = dict1['relief']
            self.Frame.takeFocus = dict1['take focus']
            self.Frame.visual = dict1['visual']
            self.Frame.width = dict1['width']
            self.FramePlace.anchor = dict1['place anchor']
            self.FramePlace.borderMode = dict1['place border mode']
            self.FramePlace.height = dict1['place height']
            self.FramePlace.width = dict1['place width']
            self.FramePlace.relHeight = dict1['place rel height']
            self.FramePlace.relWidth = dict1['place rel width']
            self.FramePlace.relX = dict1['place rel x']
            self.FramePlace.relY = dict1['place rel y']
            self.FramePlace.offsetX = dict1['place offset x']
            self.FramePlace.offsetY = dict1['place offset y']


            self.codelines.append("\n\t\tlogging.info('[gui.create_window] Creating frame widget #%d' % ")
            self.codelines.append(str(i+1))
            self.codelines.append(')')
            self.codelines.append('\n\t\tself.tkFrame[')
            self.codelines.append(str(i))
            self.codelines.append(']=tk.Frame()')
            if self.Frame.backgroundColor != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].config(background=''')
                self.codelines.append(self.Frame.backgroundColor)
                self.codelines.append("')")
            if self.Frame.borderWidth != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].config(borderwidth=')
                self.codelines.append(self.Frame.borderWidth)
                self.codelines.append(")")
            if self.Frame.colormap != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].config(colormap=''')
                self.codelines.append(self.Frame.colormap)
                self.codelines.append("')")
            if self.Frame.container != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].config(container=')
                self.codelines.append(self.Frame.container)
                self.codelines.append(")")
            if self.Frame.cursor != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].config(cursor=')
                self.codelines.append(self.Frame.cursor)
                self.codelines.append(")")
            if self.Frame.height != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].config(height=')
                self.codelines.append(self.Frame.height)
                self.codelines.append(")")
            if self.Frame.highlightBackgroundColor != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].config(highlightbackground=''')
                self.codelines.append(self.Frame.highlightBackgroundColor)
                self.codelines.append("')")
            if self.Frame.highlightColor != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].config(highlightcolor=''')
                self.codelines.append(self.Frame.highlightColor)
                self.codelines.append("')")
            if self.Frame.highlightThickness != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].config(highlightthickness=')
                self.codelines.append(self.Frame.highlightThickness)
                self.codelines.append(")")
            if self.Frame.padX != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].config(padx=')
                self.codelines.append(self.Frame.padX)
                self.codelines.append(")")
            if self.Frame.padY != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].config(pady=')
                self.codelines.append(self.Frame.padY)
                self.codelines.append(")")
            if self.Frame.relief != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append("].config(relief='")
                self.codelines.append(self.Frame.relief)
                self.codelines.append("')")
            if self.Frame.takeFocus != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].config(takefocus=')
                self.codelines.append(self.Frame.takeFocus)
                self.codelines.append(")")
            if self.Frame.visual != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].config(visual=')
                self.codelines.append(self.Frame.visual)
                self.codelines.append(")")
            if self.Frame.width != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].config(width=')
                self.codelines.append(self.Frame.width)
                self.codelines.append(")")
            self.codelines.append('\n\t\tself.tkFrame[')
            self.codelines.append(str(i))
            self.codelines.append('].place()')
            if self.FramePlace.anchor != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append("].place_configure(anchor='")
                self.codelines.append(self.FramePlace.anchor)
                self.codelines.append("')")
            if self.FramePlace.borderMode != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append("].place_configure(bordermode='")
                self.codelines.append(self.FramePlace.borderMode)
                self.codelines.append("')")
            if self.FramePlace.height != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].place_configure(height=')
                self.codelines.append(self.FramePlace.height)
                self.codelines.append(")")
            if self.FramePlace.width != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].place_configure(width=')
                self.codelines.append(self.FramePlace.width)
                self.codelines.append(")")
            if self.FramePlace.relHeight != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].place_configure(relheight=')
                self.codelines.append(self.FramePlace.relHeight)
                self.codelines.append(")")
            if self.FramePlace.relWidth != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].place_configure(relwidth=')
                self.codelines.append(self.FramePlace.relWidth)
                self.codelines.append(")")
            if self.FramePlace.relX != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].place_configure(relx=')
                self.codelines.append(self.FramePlace.relX)
                self.codelines.append(")")
            if self.FramePlace.relY != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].place_configure(rely=')
                self.codelines.append(self.FramePlace.relY)
                self.codelines.append(")")
            if self.FramePlace.offsetX != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].place_configure(x=')
                self.codelines.append(self.FramePlace.offsetX)
                self.codelines.append(")")
            if self.FramePlace.offsetY != '':
                self.codelines.append('\n\t\tself.tkFrame[')
                self.codelines.append(str(i))
                self.codelines.append('].place_configure(y=')
                self.codelines.append(self.FramePlace.offsetY)
                self.codelines.append(")")
                self.codelines.append('\n')
                self.codelines.append('\n')

        self.codelines.append('\n\t\tself.root.mainloop()')

        ################################################################################################################
        # ADD CODE TO END OF SCRIPT TO MAKE IT SELF-EXECUTING
        ################################################################################################################
        self.codelines.append('\nif __name__ == "__main__":')
        self.codelines.append("\n\tappwindow = gui('debug.log')")
        self.codelines.append('\n\tappwindow.create_window()')


        ################################################################################################################
        # ASSEMBLE LIST INTO A SINGLE STRING AND WRITE TO OUTPUT FILE
        ################################################################################################################
        self.codetowritetofile = ''.join(self.codelines)

        self.path, self.junk = os.path.split(self.inifile)
        self.outputfile = os.path.join(self.path, 'gui.py')

        f = open(self.outputfile, 'w')
        f.write(self.codetowritetofile)