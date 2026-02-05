from Utils.Reader import CRMessageReader

class Commands(CRMessageReader):
	def __init__(self, client, player, initial_bytes):
		super().__init__(initial_bytes)
		self.Client = client
		self.Player= player
		
	def decode(self):
		self.read_Vint()
		self.read_Vint()
		self.read_Vint()
		self.commandID = self.read_Vint()
	

	def process(self):
		pass


