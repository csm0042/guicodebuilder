
################################################################################################################
#IMPORT LIBRARIES
################################################################################################################
import logging
import tkinter as tk
import configparser


################################################################################################################
#DEFINE CLASS
################################################################################################################
class Window(object):
	def __init__(self):
		self.width = str()
		self.height = str()
		self.posX = str()
		self.posY = str()
		self.title = str()
		self.backgroundColor = str()
		self.title = str()


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


class Message(object):
	def __init__(self):
		self.anchor = str()
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


class Button(object):
	def __init__(self):
		self.activeBackgroundColor = str()
		self.activeForegroundColor = str()
		self.anchor = str()
		self.backgroundColor = str()
		self.bitmap = str()
		self.borderwidth = str()
		self.command = str()
		self.compound = str()
		self.cursor = str()
		self.default = str()
		self.disableForeground = str()
		self.font = str()
		self.fontSize = str()
		self.foregroundColor = str()
		self.height = str()
		self.highlightBackgroundColor = str()
		self.highlightColor = str()
		self.highlightThickness = str()
		self.image = str()
		self.justify = str()
		self.overRelief = str()
		self.padX = str()
		self.padY = str()
		self.relief = str()
		self.repeatDelay = str()
		self.repeatInterval = str()
		self.state = str()
		self.takeFocus = str()
		self.text = str()
		self.textVariable = str()
		self.underline = str()
		self.width = str()
		self.wrapLength = str()


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


################################################################################################################
#DEFINE GUI CLASS
################################################################################################################
class gui(object):
	def __init__(self, logfile):
		self.logfile = logfile
		self.root = tk.Tk()

		logging.basicConfig(level=logging.DEBUG, 
			format='%(asctime)s %(levelname)-8s %(message)s', 
			filename=self.logfile, filemode='w')
		logging.info('[gui.__init__] Appwindow object created')

		self.frameCount = 4
		self.Frame = Frame()
		self.frame_settings = Frame()
		self.FramePlace = Place()
		self.tkFrame = [tk.Frame() for i in range(self.frameCount)]
		logging.info('[gui.__init__] Found configuration data for %d frame widgets' % self.frameCount)

		self.messageCount = 2
		self.Message = Message()
		self.message_settings = Message()
		self.MessagePlace = Place()
		self.tkMessage = [tk.Message() for i in range(self.messageCount)]
		logging.info('[gui.__init__] Found configuration data for %d message widgets' % self.messageCount)

		self.textCount = 1
		self.Text = Text()
		self.text_settings = Text()
		self.TextPlace = Place()
		self.tkText = [tk.Text() for i in range(self.textCount)]
		logging.info('[gui.__init__] Found configuration data for %d text widgets' % self.textCount)

		self.buttonCount = 13
		self.Button = Button()
		self.button_settings = Button()
		self.ButtonPlace = Place()
		self.tkButton = [tk.Button() for i in range(self.buttonCount)]
		self.ButtonInput = [bool() for i in range(self.buttonCount)]
		logging.info('[gui.__init__] Found configuration data for %d button widgets' % self.buttonCount)


	################################################################################################################
	#CREATE TKINTER MAIN WINDOW
	################################################################################################################
	def create_window(self):
		logging.info('[gui.create_window] Adjusting window geometry')
		self.root.geometry("%sx%s+%s+%s" % (640, 480, 10, 10))
		self.root.title('Main')
		logging.info('[gui.create_window] Setting window title')

		logging.info('[gui.create_window] Starting frame widget loop')
		logging.info('[gui.create_window] Creating frame widget #%d' % 1)
		self.tkFrame[i] = self.create_frame_widget(self.tkFrame[i], self.Frame, self.FramePlace)
		self.tkFrame.config(height=60')
		self.tkFrame.config(relief=raised')
		self.tkFrame.config(width=640')self.tkFrame.place()
		logging.info('[gui.create_window] Creating frame widget #%d' % 2)
		self.tkFrame[i] = self.create_frame_widget(self.tkFrame[i], self.Frame, self.FramePlace)
		self.tkFrame.config(height=60')
		self.tkFrame.config(relief=raised')
		self.tkFrame.config(width=640')self.tkFrame.place()
		logging.info('[gui.create_window] Creating frame widget #%d' % 3)
		self.tkFrame[i] = self.create_frame_widget(self.tkFrame[i], self.Frame, self.FramePlace)
		self.tkFrame.config(height=360')
		self.tkFrame.config(relief=sunken')
		self.tkFrame.config(width=60')self.tkFrame.place()
		logging.info('[gui.create_window] Creating frame widget #%d' % 4)
		self.tkFrame[i] = self.create_frame_widget(self.tkFrame[i], self.Frame, self.FramePlace)
		self.tkFrame.config(height=360')
		self.tkFrame.config(relief=sunken')
		self.tkFrame.config(width=60')self.tkFrame.place()