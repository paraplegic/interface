
class Icon:
	'''
	A class to import and expose icons expressly used in the tcl/tk language
	for use within TkInter from python.
	'''

	def __init__( self, pth ):
		self.path = pth
		self.icons = {}
		self.size = None
		self.sizes = []
		self.convert()

	def convert( self ):
		'''
		An internal routine to convert from tcl/tk format to a useable form.
		'''
		all_sizes = []
		with open( self.path, 'r' ) as ic_file:
			for line in ic_file:
				s = line.split( ':' )
				tag = s[0].split( '-' )[0]
				size = s[3].split()[0]
				all_sizes.append( size )
				data = s[4]
				if not size in self.icons:
					self.icons[size] = {}
				self.icons[size][tag] = data

		sizes = set( all_sizes )
		self.sizes = list( sizes )
		self.size = self.sizes[0]

	def list( self ):
		'''
		Return a list of icon tags ...
		'''
		if not self.icons:
			self.convert()

		rv = []
		for tag, data in self.icons[self.size].items():
			rv.append( tag )

		return sorted( rv )

	def getSizes( self ):
		return self.sizes

	def getSize( self ):
		return self.size

	def setSize( self, size ):
		if size in self.sizes:
			self.size = size

	def get( self, tag ):
		'''
		Return the image data string for a specific icon tag ...
		'''
		if not self.icons:
			self.convert()

		if tag in self.icons[self.size]:
			return self.icons[self.size][tag]

		return None

