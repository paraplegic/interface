# interface
A JSON driven GUI generator using Tkinter
Most definitely not ready for prime time.

The intent is to describe the widgets, and layout using the Grid geometry manager, create event bindings and actions from the JSON descriptor, and have a run-time generation of a workable user interface.  Application code will be added manually, but the interface will be as described in the JSON.

Currently, there is a close relationship between the descriptor language and carnal knowledge of the Tk system, which is fine for those used to Tcl/TK, but given that this is designed for Python developers (ultimately), it is very likely that a higher level descriptor notation will fall out of the experience with this *PROTOTYPE* version.

