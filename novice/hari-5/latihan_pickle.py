

class SimpleObject: 

	def siswa(self, name,backward): 
		self.name = name 
		self.name_backwards = backward
		



op = SimpleObject("ahmad","aray")

SimpleObject.siswa()

print(op.name)