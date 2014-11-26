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

    def read_settings(self):
        import configparser
        Config = configparser.ConfigParser()
        Config.read(self.iniFile)
        dict1 = {}

        options = Config.options(self.section)
        for option in options:
            try:
                dict1[option] = Config.get(self.section, option)
                if dict1[option] == -1:
                    pass
            except:
                dict1[option] = None

        self.width = dict1['width']
        self.height = dict1['height']
        self.posX = dict1['pos x']
        self.posY = dict1['pos y']
        self.title = dict1['title']
        self.backgroundColor = dict1['background color']
        return self


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

    def read_settings(self):
        import configparser
        Config = configparser.ConfigParser()
        Config.read(self.iniFile)
        dict1 = {}

        options = Config.options(self.section)
        for option in options:
            try:
                dict1[option] = Config.get(self.section, option)
                if dict1[option] == -1:
                    pass
            except:
                dict1[option] = None

        self.backgroundColor = dict1['background color']
        self.borderwidth = dict1['border width']
        self.colormap = dict1['color map']
        self.container = dict1['container']
        self.cursor = dict1['cursor']
        self.height = dict1['height']
        self.highlightBackgroundColor = dict1['highlight background color']
        self.highlightColor = dict1['highlight color']
        self.highlightThickness = dict1['highlight thickness']
        self.padX = dict1['pad x']
        self.padY = dict1['pad y']
        self.relief = dict1['relief']
        self.takeFocus = dict1['take focus']
        self.visual = dict1['visual']
        self.width = dict1['width']
        return self


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

    def read_settings(self):
        import configparser
        Config = configparser.ConfigParser()
        Config.read(self.iniFile)
        dict1 = {}

        options = Config.options(self.section)
        for option in options:
            try:
                dict1[option] = Config.get(self.section, option)
                if dict1[option] == -1:
                    pass
            except:
                dict1[option] = None

        self.anchor = dict1['anchor']
        self.aspect = dict1['aspect']
        self.backgroundColor = dict1['background color']
        self.borderwidth = dict1['border width']
        self.cursor = dict1['cursor']
        self.font = dict1['font']
        self.fontSize = dict1['font size']
        self.foregroundColor = dict1['foreground color']
        self.highlightBackground = dict1['highlight background']
        self.highlightBackgroundColor = dict1['highlight background color']
        self.highlightThickness = dict1['highlight thickness']
        self.justify = dict1['justify']
        self.padX = dict1['pad x']
        self.padY = dict1['pad y']
        self.relief = dict1['relief']
        self.takeFocus = dict1['take focus']
        self.text = dict1['text']
        self.textVariable = dict1['text variable']
        self.width = dict1['width']
        return self


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

    def read_settings(self):
        Config = configparser.ConfigParser()
        Config.read(self.iniFile)
        dict1 = {}
        options = Config.options(self.section)
        for option in options:
            try:
                dict1[option] = Config.get(self.section, option)
                if dict1[option] == -1:
                    pass
            except:
                dict1[option] = None

        self.autoSeparators = dict1['auto separators']
        self.backgroundColor = dict1['background color']
        self.backgroundStipple = dict1['background stipple']
        self.borderwidth = dict1['border width']
        self.cursor = dict1['cursor']
        self.exportSelection = dict1['export selection']
        self.font = dict1['font']
        self.fontSize = dict1['font size']
        self.foregroundColor = dict1['foreground color']
        self.foregroundStipple = dict1['foreground stipple']
        self.height = dict1['height']
        self.highlightBackgroundColor = dict1['highlight background color']
        self.highlightColor = dict1['highlight color']
        self.highlightThickness = dict1['highlight thickness']
        self.insertBackground = dict1['insert background']
        self.insertBorderwidth = dict1['insert border width']
        self.insertOffTime = dict1['insert off time']
        self.insertOnTime = dict1['insert on time']
        self.insertWidth = dict1['insert width']
        self.justify = dict1['justify']
        self.lmargin1 = dict1['lmargin1']
        self.lmargin2 = dict1['lmargin2']
        self.maxUndo = dict1['max undo']
        self.padX = dict1['pad x']
        self.padY = dict1['pad y']
        self.offset = dict1['offset']
        self.overstrike = dict1['overstrike']
        self.relief = dict1['relief']
        self.rmargin = dict1['rmargin']
        self.selectBackgroundColor =dict1['select background color']
        self.selectForegroundColor = dict1['select foreground color']
        self.selectBorderwidth = dict1['select border width']
        self.setGrid = dict1['set grid']
        self.spacing1 = dict1['spacing1']
        self.spacing2 = dict1['spacing2']
        self.spacing3 = dict1['spacing3']
        self.state = dict1['state']
        self.tabs = dict1['tabs']
        self.takeFocus = dict1['take focus']
        self.text = dict1['text']
        self.underline = dict1['underline']
        self.undo = dict1['undo']
        self.width = dict1['width']
        self.wrap = dict1['wrap']
        self.xScrollCommand = dict1['x scroll command']
        self.yScrollCommand = dict1['y scroll command']
        return self


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


    def read_settings(self):
        import configparser
        Config = configparser.ConfigParser()
        Config.read(self.iniFile)
        dict1 = {}

        options = Config.options(self.section)
        for option in options:
            try:
                dict1[option] = Config.get(self.section, option)
                if dict1[option] == -1:
                    pass
            except:
                dict1[option] = None

        self.backgroundColor = dict1['background color']
        self.bitmap = dict1['bitmap']
        self.borderwidth = dict1['border width']
        self.command = dict1['command']
        self.compound = dict1['compound']
        self.cursor = dict1['cursor']
        self.default = dict1['default']
        self.disableForeground = dict1['disable foreground']
        self.font = dict1['font']
        self.fontSize = dict1['font size']
        self.foregroundColor = dict1['foreground color']
        self.height = dict1['height']
        self.highlightBackgroundColor = dict1['highlight background color']
        self.highlightColor = dict1['highlight color']
        self.highlightThickness = dict1['highlight thickness']
        self.image = dict1['image']
        self.justify = dict1['justify']
        self.overRelief = dict1['over relief']
        self.padX = dict1['pad x']
        self.padY = dict1['pad y']
        self.relief = dict1['relief']
        self.repeatDelay = dict1['repeat delay']
        self.repeatInterval = dict1['repeat interval']
        self.state = dict1['state']
        self.takeFocus = dict1['take focus']
        self.text = dict1['text']
        self.textVariable = dict1['text variable']
        self.underline = dict1['underline']
        self.width = dict1['width']
        self.wrapLength = dict1['wrap length']
        return self


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

    def read_settings(self):
        import configparser
        Config = configparser.ConfigParser()
        Config.read(self.iniFile)
        dict1 = {}

        options = Config.options(self.section)
        for option in options:
            try:
                dict1[option] = Config.get(self.section, option)
                if dict1[option] == -1:
                    pass
            except:
                dict1[option] = None

        self.anchor = dict1['place anchor']
        self.borderMode = dict1['place border mode']
        self.height = dict1['place height']
        self.width = dict1['place width']
        self.relHeight = dict1['place rel height']
        self.relWidth = dict1['place rel width']
        self.relX = dict1['place rel x']
        self.relY = dict1['place rel y']
        self.offsetX = dict1['place offset x']
        self.offsetY = dict1['place offset y']
        return self


#######################################################################################################################
# Define GUI class
#######################################################################################################################
class gui(object):
    def __init__(self, inifile, logfile):
        self.inifile = inifile
        self.logfile = logfile
        self.codestring = []
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
        self.codestring.append('\n################################################################################################################')
        self.codestring.append('\n#IMPORT LIBRARIES')
        self.codestring.append('\n################################################################################################################')
        self.codestring.append('\nimport logging')
        self.codestring.append('\nimport tkinter as tk')
        self.codestring.append('\nimport configparser')
        self.codestring.append('\n')
        self.codestring.append('\n')


        ################################################################################################################
        # DEFINE HELPER CLASSES AND MODULES
        ################################################################################################################
        self.codestring.append('\n################################################################################################################')
        self.codestring.append('\n#DEFINE CLASS')
        self.codestring.append('\n################################################################################################################')
        self.codestring.append('\nclass Window(object):')
        self.codestring.append('\n\tdef __init__(self):')
        self.codestring.append('\n\t\tself.width = str()')
        self.codestring.append('\n\t\tself.height = str()')
        self.codestring.append('\n\t\tself.posX = str()')
        self.codestring.append('\n\t\tself.posY = str()')
        self.codestring.append('\n\t\tself.title = str()')
        self.codestring.append('\n\t\tself.backgroundColor = str()')
        self.codestring.append('\n\t\tself.title = str()')
        self.codestring.append('\n')
        self.codestring.append('\n')
        self.codestring.append('\nclass Frame(object):')
        self.codestring.append('\n\tdef __init__(self):')
        self.codestring.append('\n\t\tself.backgroundColor = str()')
        self.codestring.append('\n\t\tself.borderwidth = str()')
        self.codestring.append('\n\t\tself.colormap = str()')
        self.codestring.append('\n\t\tself.container = str()')
        self.codestring.append('\n\t\tself.cursor = str()')
        self.codestring.append('\n\t\tself.height = str()')
        self.codestring.append('\n\t\tself.highlightBackgroundColor = str()')
        self.codestring.append('\n\t\tself.highlightColor = str()')
        self.codestring.append('\n\t\tself.highlightThickness = str()')
        self.codestring.append('\n\t\tself.padX = str()')
        self.codestring.append('\n\t\tself.padY = str()')
        self.codestring.append('\n\t\tself.relief = str()')
        self.codestring.append('\n\t\tself.takeFocus = str()')
        self.codestring.append('\n\t\tself.visual = str()')
        self.codestring.append('\n\t\tself.width = str()')
        self.codestring.append('\n')
        self.codestring.append('\n')
        self.codestring.append('\nclass Message(object):')
        self.codestring.append('\n\tdef __init__(self):')
        self.codestring.append('\n\t\tself.anchor = str()')
        self.codestring.append('\n\t\tself.anchor = str()')
        self.codestring.append('\n\t\tself.aspect = str()')
        self.codestring.append('\n\t\tself.backgroundColor = str()')
        self.codestring.append('\n\t\tself.borderwidth = str()')
        self.codestring.append('\n\t\tself.cursor = str()')
        self.codestring.append('\n\t\tself.font = str()')
        self.codestring.append('\n\t\tself.fontSize = str()')
        self.codestring.append('\n\t\tself.foregroundColor = str()')
        self.codestring.append('\n\t\tself.highlightBackground = str()')
        self.codestring.append('\n\t\tself.highlightBackgroundColor = str()')
        self.codestring.append('\n\t\tself.highlightThickness = str()')
        self.codestring.append('\n\t\tself.justify = str()')
        self.codestring.append('\n\t\tself.padX = str()')
        self.codestring.append('\n\t\tself.padY = str()')
        self.codestring.append('\n\t\tself.relief = str()')
        self.codestring.append('\n\t\tself.takeFocus = str()')
        self.codestring.append('\n\t\tself.text = str()')
        self.codestring.append('\n\t\tself.textVariable = str()')
        self.codestring.append('\n\t\tself.width = str()')
        self.codestring.append('\n')
        self.codestring.append('\n')
        self.codestring.append('\nclass Text(object):')
        self.codestring.append('\n\tdef __init__(self):')
        self.codestring.append('\n\t\tself.autoSeparators = str()')
        self.codestring.append('\n\t\tself.backgroundColor = str()')
        self.codestring.append('\n\t\tself.backgroundStipple = str()')
        self.codestring.append('\n\t\tself.borderwidth = str()')
        self.codestring.append('\n\t\tself.cursor = str()')
        self.codestring.append('\n\t\tself.exportSelection = str()')
        self.codestring.append('\n\t\tself.font = str()')
        self.codestring.append('\n\t\tself.fontSize = str()')
        self.codestring.append('\n\t\tself.foregroundColor = str()')
        self.codestring.append('\n\t\tself.foregroundStipple = str()')
        self.codestring.append('\n\t\tself.height = str()')
        self.codestring.append('\n\t\tself.highlightBackgroundColor = str()')
        self.codestring.append('\n\t\tself.highlightColor = str()')
        self.codestring.append('\n\t\tself.highlightThickness = str()')
        self.codestring.append('\n\t\tself.insertBackground = str()')
        self.codestring.append('\n\t\tself.insertBorderwidth = str()')
        self.codestring.append('\n\t\tself.insertOffTime = str()')
        self.codestring.append('\n\t\tself.insertOnTime = str()')
        self.codestring.append('\n\t\tself.insertWidth = str()')
        self.codestring.append('\n\t\tself.justify = str()')
        self.codestring.append('\n\t\tself.lmargin1 = str()')
        self.codestring.append('\n\t\tself.lmargin2 = str()')
        self.codestring.append('\n\t\tself.maxUndo = str()')
        self.codestring.append('\n\t\tself.padX = str()')
        self.codestring.append('\n\t\tself.padY = str()')
        self.codestring.append('\n\t\tself.offset = str()')
        self.codestring.append('\n\t\tself.overstrike = str()')
        self.codestring.append('\n\t\tself.relief = str()')
        self.codestring.append('\n\t\tself.rmargin = str()')
        self.codestring.append('\n\t\tself.selectBackgroundColor = str()')
        self.codestring.append('\n\t\tself.selectForegroundColor = str()')
        self.codestring.append('\n\t\tself.selectBorderwidth = str()')
        self.codestring.append('\n\t\tself.setGrid = str()')
        self.codestring.append('\n\t\tself.spacing1 = str()')
        self.codestring.append('\n\t\tself.spacing2 = str()')
        self.codestring.append('\n\t\tself.spacing3 = str()')
        self.codestring.append('\n\t\tself.state = str()')
        self.codestring.append('\n\t\tself.tabs = str()')
        self.codestring.append('\n\t\tself.takeFocus = str()')
        self.codestring.append('\n\t\tself.text = str()')
        self.codestring.append('\n\t\tself.underline = str()')
        self.codestring.append('\n\t\tself.undo = str()')
        self.codestring.append('\n\t\tself.width = str()')
        self.codestring.append('\n\t\tself.wrap = str()')
        self.codestring.append('\n\t\tself.xScrollCommand = str()')
        self.codestring.append('\n\t\tself.yScrollCommand = str()')
        self.codestring.append('\n')
        self.codestring.append('\n')
        self.codestring.append('\nclass Button(object):')
        self.codestring.append('\n\tdef __init__(self):')
        self.codestring.append('\n\t\tself.activeBackgroundColor = str()')
        self.codestring.append('\n\t\tself.activeForegroundColor = str()')
        self.codestring.append('\n\t\tself.anchor = str()')
        self.codestring.append('\n\t\tself.backgroundColor = str()')
        self.codestring.append('\n\t\tself.bitmap = str()')
        self.codestring.append('\n\t\tself.borderwidth = str()')
        self.codestring.append('\n\t\tself.command = str()')
        self.codestring.append('\n\t\tself.compound = str()')
        self.codestring.append('\n\t\tself.cursor = str()')
        self.codestring.append('\n\t\tself.default = str()')
        self.codestring.append('\n\t\tself.disableForeground = str()')
        self.codestring.append('\n\t\tself.font = str()')
        self.codestring.append('\n\t\tself.fontSize = str()')
        self.codestring.append('\n\t\tself.foregroundColor = str()')
        self.codestring.append('\n\t\tself.height = str()')
        self.codestring.append('\n\t\tself.highlightBackgroundColor = str()')
        self.codestring.append('\n\t\tself.highlightColor = str()')
        self.codestring.append('\n\t\tself.highlightThickness = str()')
        self.codestring.append('\n\t\tself.image = str()')
        self.codestring.append('\n\t\tself.justify = str()')
        self.codestring.append('\n\t\tself.overRelief = str()')
        self.codestring.append('\n\t\tself.padX = str()')
        self.codestring.append('\n\t\tself.padY = str()')
        self.codestring.append('\n\t\tself.relief = str()')
        self.codestring.append('\n\t\tself.repeatDelay = str()')
        self.codestring.append('\n\t\tself.repeatInterval = str()')
        self.codestring.append('\n\t\tself.state = str()')
        self.codestring.append('\n\t\tself.takeFocus = str()')
        self.codestring.append('\n\t\tself.text = str()')
        self.codestring.append('\n\t\tself.textVariable = str()')
        self.codestring.append('\n\t\tself.underline = str()')
        self.codestring.append('\n\t\tself.width = str()')
        self.codestring.append('\n\t\tself.wrapLength = str()')
        self.codestring.append('\n')
        self.codestring.append('\n')
        self.codestring.append('\nclass Place(object):')
        self.codestring.append('\n\tdef __init__(self):')
        self.codestring.append('\n\t\tself.anchor = str()')
        self.codestring.append('\n\t\tself.borderMode = str()')
        self.codestring.append('\n\t\tself.height = str()')
        self.codestring.append('\n\t\tself.width = str()')
        self.codestring.append('\n\t\tself.relHeight = str()')
        self.codestring.append('\n\t\tself.relWidth = str()')
        self.codestring.append('\n\t\tself.relX = str()')
        self.codestring.append('\n\t\tself.relY = str()')
        self.codestring.append('\n\t\tself.offsetX = str()')
        self.codestring.append('\n\t\tself.offsetY = str()')
        self.codestring.append('\n')
        self.codestring.append('\n')







        ################################################################################################################
        # DEFINE GUI CLASS AND ADD __init__ METHOD
        ################################################################################################################
        self.codestring.append('\n################################################################################################################')
        self.codestring.append('\n#DEFINE GUI CLASS')
        self.codestring.append('\n################################################################################################################')
        self.codestring.append('\nclass gui(object):')
        self.codestring.append('\n\tdef __init__(self, logfile):')
        self.codestring.append('\n\t\tself.logfile = logfile')
        self.codestring.append('\n\t\tself.root = tk.Tk()')
        self.codestring.append('\n')
        self.codestring.append('\n\t\tlogging.basicConfig(level=logging.DEBUG, ')
        self.codestring.append('''\n\t\t\tformat='%(asctime)s %(levelname)-8s %(message)s', ''')
        self.codestring.append('''\n\t\t\tfilename=self.logfile, filemode='w')''')
        self.codestring.append('''\n\t\tlogging.info('[gui.__init__] Appwindow object created')''')
        self.codestring.append('\n')
        self.codestring.append('\n\t\tself.frameCount = ')
        self.codestring.append(str(CountWidgetByType(self.inifile, "frame")))
        self.codestring.append('\n\t\tself.Frame = Frame()')
        self.codestring.append('\n\t\tself.frame_settings = Frame()')
        self.codestring.append('\n\t\tself.FramePlace = Place()')
        self.codestring.append('\n\t\tself.tkFrame = [tk.Frame() for i in range(self.frameCount)]')
        self.codestring.append("\n\t\tlogging.info('[gui.__init__] Found configuration data for %d frame widgets' % self.frameCount)")
        self.codestring.append('\n')
        self.codestring.append('\n\t\tself.messageCount = ')
        self.codestring.append(str(CountWidgetByType(self.inifile, "message")))
        self.codestring.append('\n\t\tself.Message = Message()')
        self.codestring.append('\n\t\tself.message_settings = Message()')
        self.codestring.append('\n\t\tself.MessagePlace = Place()')
        self.codestring.append('\n\t\tself.tkMessage = [tk.Message() for i in range(self.messageCount)]')
        self.codestring.append("\n\t\tlogging.info('[gui.__init__] Found configuration data for %d message widgets' % self.messageCount)")
        self.codestring.append('\n')
        self.codestring.append('\n\t\tself.textCount = ')
        self.codestring.append(str(CountWidgetByType(self.inifile, "text")))
        self.codestring.append('\n\t\tself.Text = Text()')
        self.codestring.append('\n\t\tself.text_settings = Text()')
        self.codestring.append('\n\t\tself.TextPlace = Place()')
        self.codestring.append('\n\t\tself.tkText = [tk.Text() for i in range(self.textCount)]')
        self.codestring.append("\n\t\tlogging.info('[gui.__init__] Found configuration data for %d text widgets' % self.textCount)")
        self.codestring.append('\n')
        self.codestring.append('\n\t\tself.buttonCount = ')
        self.codestring.append(str(CountWidgetByType(self.inifile, "button")))
        self.codestring.append('\n\t\tself.Button = Button()')
        self.codestring.append('\n\t\tself.button_settings = Button()')
        self.codestring.append('\n\t\tself.ButtonPlace = Place()')
        self.codestring.append('\n\t\tself.tkButton = [tk.Button() for i in range(self.buttonCount)]')
        self.codestring.append('\n\t\tself.ButtonInput = [bool() for i in range(self.buttonCount)]')
        self.codestring.append("\n\t\tlogging.info('[gui.__init__] Found configuration data for %d button widgets' % self.buttonCount)")
        self.codestring.append('\n')
        self.codestring.append('\n')



        ################################################################################################################
        # CREATE TKINTER MAIN WINDOW
        ################################################################################################################
        self.Window.section = "main window"
        self.Window.iniFile = self.inifile
        self.Window = Window.read_settings(self.Window)
        self.codestring.append('\n\t################################################################################################################')
        self.codestring.append('\n\t#CREATE TKINTER MAIN WINDOW')
        self.codestring.append('\n\t################################################################################################################')
        self.codestring.append('\n\tdef create_window(self):')
        self.codestring.append('''\n\t\tlogging.info('[gui.create_window] Adjusting window geometry')''')

        self.codestring.append('''\n\t\tself.root.geometry("%sx%s+%s+%s" % (''')
        self.codestring.append(self.Window.width)
        self.codestring.append(', ')
        self.codestring.append(self.Window.height)
        self.codestring.append(', ')
        self.codestring.append(self.Window.posX)
        self.codestring.append(', ')
        self.codestring.append(self.Window.posY)
        self.codestring.append('))')

        if self.Window.backgroundColor != "":
            self.codestring.append('\n\t\tself.root.config(background=')
            self.codestring.append(self.Window.backgroundColor)
            self.codestring.append(')')
            self.codestring.append('''\n\t\tlogging.info('[gui.create_window] Adjusting window background color')''')

        if self.Window.title != '':
            self.codestring.append("\n\t\tself.root.title('")
            self.codestring.append(self.Window.title)
            self.codestring.append("')")
            self.codestring.append('''\n\t\tlogging.info('[gui.create_window] Setting window title')''')

        self.codestring.append('\n')


        ################################################################################################################
        # CALL LOOP TO CREATE FRAME WIDGETS
        ################################################################################################################
        self.codestring.append("\n\t\tlogging.info('[gui.create_window] Starting frame widget loop')")
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


            self.codestring.append("\n\t\tlogging.info('[gui.create_window] Creating frame widget #%d' % ")
            self.codestring.append(str(i+1))
            self.codestring.append(')')
            if self.Frame.backgroundColor != '':
                self.codestring.append('\n\t\tself.tkFrame[')
                self.codestring.append(i)
                self.codestring.append('].config(background=')
                self.codestring.append(self.Frame.backgroundColor)
                self.codestring.append("')")
            if self.Frame.borderwidth != '':
                self.codestring.append('\n\t\tself.tkFrame[')
                self.codestring.append(i)
                self.codestring.append('].config(borderwidth=')
                self.codestring.append(self.Frame.borderwidth)
                self.codestring.append("')")
            if self.Frame.colormap != '':
                self.codestring.append('\n\t\tself.tkFrame['
                self.codestring.append(i)
                self.codestring.append('].config(colormap=')
                self.codestring.append(self.Frame.colormap)
                self.codestring.append("')")
            if self.Frame.container != '':
                self.codestring.append('\n\t\tself.tkFrame.config(container=')
                self.codestring.append(i)

                self.codestring.append(self.Frame.container)
                self.codestring.append("')")
            if self.Frame.cursor != '':
                self.codestring.append('\n\t\tself.tkFrame.config(cursor=')
                self.codestring.append(i)

                self.codestring.append(self.Frame.cursor)
                self.codestring.append("')")
            if self.Frame.height != '':
                self.codestring.append('\n\t\tself.tkFrame.config(height=')
                self.codestring.append(i)

                self.codestring.append(self.Frame.height)
                self.codestring.append("')")
            if self.Frame.highlightBackgroundColor != '':
                self.codestring.append('\n\t\tself.tkFrame.config(highlightbackground=')
                self.codestring.append(i)

                self.codestring.append(self.Frame.highlightBackgroundColor)
                self.codestring.append("')")
            if self.Frame.highlightColor != '':
                self.codestring.append('\n\t\tself.tkFrame.config(highlightcolor=')
                self.codestring.append(i)

                self.codestring.append(self.Frame.highlightColor)
                self.codestring.append("')")
            if self.Frame.highlightThickness != '':
                self.codestring.append('\n\t\tself.tkFrame.config(highlightthickness=')
                self.codestring.append(i)

                self.codestring.append(self.Frame.highlightThickness)
                self.codestring.append("')")
            if self.Frame.padX != '':
                self.codestring.append('\n\t\tself.tkFrame.config(padx=')
                self.codestring.append(i)

                self.codestring.append(self.Frame.padX)
                self.codestring.append("')")
            if self.Frame.padY != '':
                self.codestring.append('\n\t\tself.tkFrame.config(pady=')
                self.codestring.append(i)

                self.codestring.append(self.Frame.padY)
                self.codestring.append("')")
            if self.Frame.relief != '':
                self.codestring.append('\n\t\tself.tkFrame.config(relief=')
                self.codestring.append(i)

                self.codestring.append(self.Frame.relief)
                self.codestring.append("')")
            if self.Frame.takeFocus != '':
                self.codestring.append('\n\t\tself.tkFrame.config(takefocus=')
                self.codestring.append(i)

                self.codestring.append(self.Frame.takeFocus)
                self.codestring.append("')")
            if self.Frame.visual != '':
                self.codestring.append('\n\t\tself.tkFrame.config(visual=')
                self.codestring.append(i)

                self.codestring.append(self.Frame.visual)
                self.codestring.append("')")
            if self.Frame.width != '':
                self.codestring.append('\n\t\tself.tkFrame.config(width=')
                self.codestring.append(i)

                self.codestring.append(self.Frame.width)
                self.codestring.append("')")
            self.codestring.append('self.tkFrame.place()')
            if self.FramePlace.anchor != '':
                self.codestring.append('\n\t\tself.tkFrame.place_configure(anchor=')
                self.codestring.append(i)

                self.codestring.append(self.FramePlace.anchor)
                self.codestring.append("')")
            if self.FramePlace.borderMode != '':
                self.codestring.append('\n\t\tself.tkFrame.place_configure(bordermode=')
                self.codestring.append(i)

                self.codestring.append(self.FramePlace.borderMode)
                self.codestring.append("')")
            if self.FramePlace.height != '':
                self.codestring.append('\n\t\tself.tkFrame.place_configure(height=')
                self.codestring.append(i)

                self.codestring.append(self.FramePlace.height)
                self.codestring.append("')")
            if self.FramePlace.width != '':
                self.codestring.append('\n\t\tself.tkFrame[')
                self.codestring.append(str(i))
                self.codestring.append('].place_configure(width=')
                self.codestring.append(self.FramePlace.width)
                self.codestring.append("')")
            if self.FramePlace.relHeight != '':
                self.codestring.append('\n\t\tself.tkFrame[')
                self.codestring.append(str(i))
                self.codestring.append('].place_configure(relheight=')
                self.codestring.append(self.FramePlace.relHeight)
                self.codestring.append("')")
            if self.FramePlace.relWidth != '':
                self.codestring.append('\n\t\tself.tkFrame[')
                self.codestring.append(str(i))
                self.codestring.append('].place_configure(relwidth=')
                self.codestring.append(self.FramePlace.relWidth)
                self.codestring.append("')")
            if self.FramePlace.relX != '':
                self.codestring.append('\n\t\tself.tkFrame[')
                self.codestring.append(str(i))
                self.codestring.append('].place_configure(relx=')
                self.codestring.append(self.FramePlace.relX)
                self.codestring.append("')")
            if self.FramePlace.relY != '':
                self.codestring.append('\n\t\tself.tkFrame[')
                self.codestring.append(str(i))
                self.codestring.append('].place_configure(rely=')
                self.codestring.append(self.FramePlace.relY)
                self.codestring.append("')")
            if self.FramePlace.offsetX != '':
                self.codestring.append('\n\t\tself.tkFrame[')
                self.codestring.append(str(i))
                self.codestring.append('].place_configure(x=')
                self.codestring.append(self.FramePlace.offsetX)
                self.codestring.append("')")
            if self.FramePlace.offsetY != '':
                self.codestring.append('\n\t\tself.tkFrame[')
                self.codestring.append(str(i))
                self.codestring.append('].place_configure(y=')
                self.codestring.append(self.FramePlace.offsetY)
                self.codestring.append("')")







        ################################################################################################################
        # ASSEMBLE LIST INTO A SINGLE STRING AND WRITE TO OUTPUT FILE
        ################################################################################################################
        self.codetowritetofile = ''.join(self.codestring)

        self.path, self.junk = os.path.split(self.inifile)
        self.outputfile = os.path.join(self.path, 'gui.py')

        f = open(self.outputfile, 'w')
        f.write(self.codetowritetofile)