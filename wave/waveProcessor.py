import wave

#Realizar os inputs

with wave.open('music.wav', mode='rb') as file:
	
	print('\nInfo about: ')
	info = file.getparams()
	print('- Number of channels: ' + str(info[0]))
	print('- Number of frames: ' + str(info[1]))
	print('- Sample width: ' + str(info[2]))
	print('- Frame rate: ' + str(info[3]) + '\n\n')

	frames = list(range(1,info[3]))
	file.rewind()
	right = []
	left = []

	for i in range(0, info[3]):
		aux = file.readframes(1)
		print(str(aux))
		
		#print('aux: ' + str(aux) + ' [4:6]: ' + str(aux[4:6]) + 'hex: ' + str(int(aux[4:6], 16)))
		#left.append(int(aux[4:6], 16))
		#right.append(int(aux[4:6], 16))

		
	plt.plot(left, frames)
	plt.plot(right, frames)

