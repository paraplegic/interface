
class Icon:
	'''
	A class to import and expose icons expressly used in the tcl/tk language
	for use within TkInter from python.
	'''

	def __init__( self, pth ):
		self.path = pth
		self.info = None
		pass

	def convert( self ):
		'''
		An internal routine to convert from tcl/tk format to a useable form.
		'''
		self.info = {}
		with open( self.path, 'r' ) as ic_file:
			for line in ic_file:
				s = line.split( ':' )
				tag = s[0]
				size = s[3].split()[0]
				data = s[4]
				entry = { "size" : size, "data" : data }
				self.info[tag] = entry

	def list( self ):
		'''
		Return a list of icon tags ...
		'''
		if not self.info:
			self.convert()
		return self.info.keys()

	def get( self, tag ):
		'''
		Return the image data string for a specific icon tag ...
		'''
		if not self.info:
			self.convert()

		if tag in self.info:
			return self.info[tag]['data']

		return None

