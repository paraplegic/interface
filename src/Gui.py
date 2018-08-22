import Tkinter as Tk
import ttk as ttk

class X( Tk.Tk ):

	root = ""

	def __init__( self, *args, **kwargs ):
		Tk.Tk.__init__( self )
		self.icons = None
		self.images = {}
		self.vars = {}
		self.widgets = {}
		self.widgets['root'] = self
		self.widgets['root'].grid_columnconfigure( 0, weight=1 )
		self.widgets['root'].grid_rowconfigure( 0, weight=1 )

	def exitApplication( self ):
		self.destroy()

	def setTheme( self, event ):
		x = ttk.Style()
		if self.vars['myTheme'].get() in x.theme_names():
			newTheme = self.vars['myTheme'].get()
			x.theme_use( newTheme )
			return 1
		return 0

	def setIcons( self, icons ):
		self.icons = icons

	def getIconData( self, tag ):
		return self.icons.get( tag )

	def getIconImage( self, tag ):
		if not tag in self.images:
			self.images[tag] = Tk.PhotoImage( data=self.getIconData( tag ) )
		return self.images[tag]

	def addWidget( self, parent, w, conf ):
		widget = str( conf['widget'] )
		s = widget + "( self.widgets['%s'] )" % parent
		d = None
		if 'opts' in conf:
			d = conf['opts']
			s = widget + "( self.widgets['%s'], **%s )" % (parent, d) 

		self.widgets[w] = eval( s )

		if 'args' in conf:
			if 'textvariable' in conf['args']:
				myvar = conf['args']['textvariable']
				self.vars[myvar] = Tk.StringVar()
				conf['args']['textvariable'] = self.vars[myvar]
				
			self.cnfWidget( w, **conf['args'] )

		if 'add' in conf:
			kwrgs = conf['add']
			dad = kwrgs.pop( 'parent' )
			self.widgets[dad].add( self.widgets[w], **kwrgs )

		if 'grid' in conf:
			self.widgets[w].grid( conf['grid'] )

		if 'col_weight' in conf:
			self.colWeight( w, conf['col_weight'] )

		if 'row_weight' in conf:
			self.rowWeight( w, conf['row_weight'] )

		if 'scroll' in conf:
			print "scroll: ", parent, w
			self.addScrollbars( self.widgets[parent], self.widgets[w], conf['scroll'] )

		if 'bind' in conf:
			s = 'self.widgets[w].bind( "%s", %s )' % ( conf['bind']['event'], conf['bind']['binding'] )
			eval( s )

		if 'icon' in conf:
			img = self.getIconImage( conf['icon'] )
			self.widgets[w].configure( image=img )

		return ( w, widget )

	def cnfWidget( self, w, **kwargs ):
		if 'command' in kwargs:
			cmd = eval( kwargs['command'] )
			self.widgets[w].configure( command=cmd )
			kwargs.pop( 'command' )

		self.widgets[w].configure( kwargs )

	def colWeight( self, w, conf ):
		## containers can specify column configuration/weights ...
		ix = 0
		for wgt in conf:
			self.widgets[w].grid_columnconfigure( ix, weight=wgt )
			ix += 1

	def rowWeight( self, w, conf ):
		## containers can specify row configuration/weights ...
		ix = 0
		for wgt in conf:
			self.widgets[w].grid_rowconfigure( ix, weight=wgt )
			ix += 1

	def addScrollbars( self, parent, w, conf ):
		if 'x' in conf:
			xsb = ttk.Scrollbar( parent, orient='horizontal' )
			xsb.grid( row=1, column=0, sticky="new" )
			xsb.config( command=w.xview)
			w.config( xscrollcommand=xsb.set)
			parent.grid_columnconfigure( 0, weight=10 )
			parent.grid_columnconfigure( 1, weight=1 )

		if 'y' in conf:
			ysb = ttk.Scrollbar( parent )
			ysb.grid( row=0, column=1, sticky="wns" )
			ysb.config( command=w.yview)
			w.config( yscrollcommand=ysb.set)
			parent.grid_rowconfigure( 0, weight=10 )
			parent.grid_rowconfigure( 1, weight=1 )

	def getWidget( self, tag ):
		return self.widgets[tag]

if __name__ == '__main__':
    main()
