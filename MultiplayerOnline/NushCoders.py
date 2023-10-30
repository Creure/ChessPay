# -*- coding:utf8 -*-

class NushCoders:
	
	def __init__(self, password="BA61-01407A"):

		self.__CharacterEncrypt = {
						"a" : 199, "b": 276, "c": 302, "d":455 , "e":587, 
						"f": 672, "g":738, "h":845, "i":932 , "j": 1024, "k":1234
						,"l": 1345, "m":1482, "n":1592, "o":1677, "p": 1782, 
						"q":1892, "r":1972, "s":20399, "t": 21882, "u":22244,
						"v":23441, "w":24555, "x":25163, "y":26383, "z":27649, 
						":":28645, "=":29876, "[": 304777, "]": 318484, "{":324533, 
						"}":334532, ".":345567, "<":352384, ">":364422, "(":372747, 
						")":385840, "+":392842, "-":4032041, "'":4188294, '"':4274829,
						"*":4375894, "@":4485932, "#":4567943, "$":4683739, "%":4783829,
						"&":48859448, "!":49596283,"^":507776840, "ψ":517281937, "ñ":527896753,
						"?":53837483, "¿":54678764, "_":55374837, "é":56839473, ",":578493827,
						"\n":59847232, "\r":60898767, "|":71728372, "∼":72839283,
						"0": "Ø", "1":"ß", "2": "¶", "3":"æ", "4": "¿","5":"¾", 
						"6":"Σ", "7":"μ", "8" :"ψ", "9":"∀","/":"⌊", ' ': "€", 
						}

		self.__character_separate = ("!","@", "#" , "$", 
									"%", "^", "&", "*")
		
		def __convertPassword(pasword):
			self.num = ["1","2","3","4","5","6","7","8","9", "0"]
			text = ""
			try:
				for char in password:
					if char in self.__CharacterEncrypt.keys() or char in self.num:
						if char in self.num:
							text = text + char

						elif char.isupper() == True:
							text = text + str(self.__CharacterEncrypt[char.lower()]*4)

						else:
							text = text + str(self.__CharacterEncrypt[char]*2)
					else:
						text = text +str(ord(char)*8)


				return text.replace("€", "")
			except Exception as e:
				from colorama import Fore
				import sys
				print(Fore.RED + ">YhhSPConve>404" + str(e))
				sys.exit(0)
		
		self.__password = int(__convertPassword(password)) * 1024 	

	def encryption(self, word):
		import random
		self.word = word
		text = ""

		x = self.__password
		
		try:
			for i in word:
				Upper = i.isupper()
				
				for byte in range(1024):
						div = random.choice(self.__character_separate)
				
				if i.lower() in self.__CharacterEncrypt.keys():

					if Upper == False:
						Type = type(self.__CharacterEncrypt[i])
					else: 
						Type = int
					
					if Type == int:
						
						if Upper == False:
							text = text + str(self.__CharacterEncrypt[i] * x) + div
						else:
							text = text + str(self.__CharacterEncrypt[i.lower()] * 1024 * x) + div
					else:
						text = text + self.__CharacterEncrypt[i] + div

				else:
					for EC in range(32, 255):
						if chr(EC) == i:
							text = text + str(EC * x ) + div
		except Exception as e:
			return e
		return text




	def decoded(self,word):
		self.word = word
		decodedText = ""
		block_Code = []
		block = ""
		x = self.__password


		for i in self.word:
			
			if i in self.__character_separate:
				block_Code.append(block)
				block = ""
				continue
			
			block = block + i

		
		for i in block_Code:
			character = i
			keys = list(self.__CharacterEncrypt.keys())
			for i in self.num:
				keys.remove(i)

			for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
				keys.append(i)

			for y in keys:#
				
				if y.isupper() == False:
					if type(self.__CharacterEncrypt[y]) != str:
						
						test = str(self.__CharacterEncrypt[y] * x)
						if character == test:
							decodedText = decodedText + y
				else:
					test = str(self.__CharacterEncrypt[y.lower()] * 1024 *x)
					if character == test:
						decodedText = decodedText + y

			
			for y in (" 0123456789"):

				text = self.__CharacterEncrypt[y]			
				if character == text:
						decodedText = decodedText + y
						continue

			for CS in range(32,255):
				f = CS * x

				if f == i:
					decodedText = decodedText + chr(CS)
		
		return decodedText