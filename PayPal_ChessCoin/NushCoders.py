# -*- coding:utf8 -*-
import random
from colorama import Fore
import sys
import zlib
class ChessCoinEncription:
	
	def __init__(self, password="BA61-01407A"):

		self.__CharacterEncrypt = {
				 "a": 472839, "b": 583920, "c": 619482, "d": 732904, "e": 847192,
				"f": 921750, "g": 1045873, "h": 1157369, "i": 1293845, "j": 1348202,
				"k": 1482735, "l": 1598203, "m": 1674923, "n": 1749831, "o": 1894302,
				"p": 1962847, "q": 2074832, "r": 2147903, "s": 2234678, "t": 2389421,
				"u": 2491830, "v": 2571934, "w": 2637481, "x": 2758390, "y": 2872934,
				"z": 2958471, ":": 3047385, "=": 3150924, "[": 3274856, "]": 3387101,
				"{": 3498193, "}": 3584730, ".": 3693842, "<": 3748290, ">": 3871029,
				"(": 3965728, ")": 4056934, "+": 4162031, "-": 4271029, "'": 4369824,
				'"': 4482037, "*": 4598239, "@": 4689204, "#": 4791382, "$": 4892394,
				"%": 4982735, "&": 5073842, "!": 5182904, "^": 5271938, "ψ": 5362091,
				"ñ": 5478392, "?": 5569213, "¿": 5673849, "_": 5782039, "é": 5892348,
				",": 5984731, "\n": 6092832, "\r": 6184932, "|": 6284912, "∼": 6392847,
				"0": 6429834, "1": 6540921, "2": 6654832, "3": 6784923, "4": 6892034,
				"5": 6948271, "6": 7024831, "7": 7152394, "8": 7283942, "9": 7392841,
				"/": 7458293, ' ': 7583941, 
				"0": "Ø", "1": "ß", "2": "¶", "3": "æ", "4": "¿", "5": "¾",
				"6": "Σ", "7": "μ", "8": "ψ", "9": "∀", "/": "⌊", ' ': "€"
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
				print(Fore.RED + ">YhhSPConve>404" + str(e))
				sys.exit(0)
		
		self.__password = int(__convertPassword(password)) * 1024 	

	def encryption(self, word):
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
		
		
		return zlib.compress(text.encode('utf-8'))




	def decoded(self,word):
		self.word = zlib.decompress(word).decode('utf-8')
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