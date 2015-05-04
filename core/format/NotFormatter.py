from core.format.FileFormatter import FileFormatter

class NotFormatter(FileFormatter):
    def format(self, directory):
        #print( "No se puede aplicar formato "+directory )
	def __init__(self):
		FileFormatter.__init__(self)
