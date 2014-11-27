guicodebuilder
==========

This package can be used to create a python file containing a class and associated methods that can be called to
generate a GUI for an application.  The layout and content of the GUI is determined by parameters entered into an
INI file which the code then interprets and uses to write a custom python file containing a class and methods specific
to that specific GUI layout and content.  The resulting file "gui.py" can then be imported and used in other python
applications and packages, simplifying the creation of the GUI that you would otherwise have to code along with the
rest of the application code.

The current applicaton support tkinter windows, frames, message widgets, text widgets, and button widgets.  For usability-sake,
a "callback" method is automatically added whenever an application file is generated containing buttons.  This callback method
automatically expands so contain an entry for each button defined in the application.  By default, none of the buttons do anything
other than log that they were pressed to the logfile (with one exception).  It is up to the user to add whatever functiosn are
required manually once the initial code is auto-generated and the "gui.py" file is moved over to the target application.  Just
to serve as an example, button #1 is pre-set-up in the callback method to terminate the root application window.
