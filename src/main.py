#!/usr/bin/env python

import os
import sys
import json
import random

from Gui import X
from Icon import Icon

app = None

def get_config( pth ):
	''' get configuration from json '''
	if not os.path.exists( pth ):
		return None

	try:
		rv = json.load( open( pth, 'rb' ) )

	except ValueError as e:
		print "unable to parse configuration file %s (%s)." % (pth,e)
		return None

	return rv

def walkConfig( app, p, w ):
	print w['tag']
	tag, typ = app.addWidget( p, w['tag'], w )
	if 'children' in w:
		for x in w['children']: 
			walkConfig( app, w['tag'], x )

def table_addRow( tv, *args ):
	tags = [ 'even', 'odd' ]
	siz = len( tv.get_children() )
	tv.insert( '', 'end', values=args[0], tags=( tags[siz%2], ) )

def table_addColumns( tv, args ):
	tv['show'] = 'headings'  ## kill the empty column for ID
	tv['columns'] = args     ## set the column names ...

	tv.tag_configure('even', background='white')
	tv.tag_configure('odd', background='#EAECEE')
	for a in args:
		tv.column( a, width=12, stretch = True, anchor='center' )
		tv.heading( a, text=a.capitalize() )

def drawIcons( app, tab, cnv, icons, lbl ):
	r = 10
	c = 80
	max_y = 0
	canvas = app.widgets[cnv]
	iclist = icons.list()
	app.cnfWidget( tab, **{ "text" : lbl+' (%d icons)' % len(iclist) } )
	for ic in iclist:
		conf = { "tag" : ic, "widget" : "ttk.Label", "icon" : ic, "args": { "text" : ic, "compound" : "left" }, "grid" : { "row": r, "column" : c } }
		app.addWidget( cnv, ic, conf )
		canvas.create_window( c, r, window=app.widgets[ic] )
		r += 30
		if r > max_y:
			max_y = r
		if r > 9970:
			r = 10
			c += 200

	canvas.configure( scrollregion=canvas.bbox( "all" ) )

		
def main( args ):

	global app
	app = X()

	ikons=Icon( 'Icons/tkIcons-sample.ikons' )
	kde=Icon( 'Icons/tkIcons-sample.kde' )
	slick=Icon( 'Icons/tkIcons-sample.slick' )
	crystal=Icon( 'Icons/tkIcons-sample.crystal' )
	app.setIcons( crystal )

	cnf = get_config( args[1] )
	if not cnf:
		print "::: Error aborted."
		exit( 1 )

	for o in cnf['children']:
		walkConfig( app, 'root', o )

	t = app.getWidget( "t1" )
	table_addColumns( t, [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven" ] )
	for ix in range( 120 ):
		table_addRow( t, [random.uniform(0.0,100.0) for _ in xrange(12)] )

	app.setIcons( crystal )
	drawIcons( app, "tab1", "cnv1", crystal, 'crystal' )

	app.setIcons( slick )
	drawIcons( app, "tab2", "cnv2", slick, 'slick' )

	app.setIcons( kde )
	drawIcons( app, "tab3", "cnv3", kde, 'kde' )

	app.setIcons( ikons )
	drawIcons( app, "tab4", "cnv4", ikons, 'ikons' )

	app.mainloop()

if __name__ == '__main__':
	main( sys.argv )
