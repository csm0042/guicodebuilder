## WINDOW
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


## FRAME
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

## MESSAGE
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

## TEXT
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


## BUTTON
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


## PLACE
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
