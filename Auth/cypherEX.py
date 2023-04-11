import time
import random 
import matplotlib.pyplot as plt
import timeit
start = time.time()

class cypherEX():		
	def cypheration(self, code_param, weight=60):
		import time
		year, month, day, hour, minute, secunde = time.strftime("%Y,%m,%d,%I,%M,%S").split(',')
		seed = (int(year)/int(month)) + (int(month) + int(day) + int(hour) + int(minute)) ** int(secunde)
		weight = weight
		print "seed -> ", seed

		code = code_param
		random.seed(seed);

		key = random.random() #primary key
		key_constelacion = ((random.uniform(weight, seed))/(seed/key)) #constelation_key

		def bias(char):
			bias = random.random()
			return bias * ord(char)

		def generate_random_key_list(key, key_constelacion):
			secret_key = []
			for i in range(0,10):
				data = (i)/(key)*((key-1)**key_constelacion**time.time()) + weight
				if(data>128):
					data = data/4
				secret_key.append(data)
			return secret_key

		def generate_word(code):
			word_complete = ""
			for i in range(0,len(code)):
				word_complete = word_complete + (code[i] + '.')
			return word_complete.split('.')

		def encode(word, list_keys):
			for i in range(0, len(word)-1):
				word[i] = repr(list_keys[random.randint(0,9)])

			word_encode = word
			return word_encode

		def decode(word_encode):
			output_word = []
			for i in range(0, len(word_encode)-1):
				output_word.append(str(unichr(int(float(word_encode[i])))))
			return output_word

		#random values to the key
		testing_list = generate_random_key_list(key, key_constelacion)
		print testing_list

		#recive the word
		word_complete = generate_word(code)
  
		bias_List = []
		for value in word_complete[:len(word_complete)-1]:
			print(value)
			bias_List.append(bias(value))
		
		print bias_List
		#write the encrypt word
		print word_complete

		#abstract the information
		word_encode = encode(word_complete, testing_list)
		print word_encode

		#To text
		print decode(word_encode)

		word_final = ''.join(decode(word_encode))
		print word_final 

		end = time.time()

		print "time required" 
		print(end-start)

		return word_final


