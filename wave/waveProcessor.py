import matplotlib.pyplot as plt
import numpy as np
import wave

#Realizar os inputs

with wave.open('bird-1.wav', mode='rb') as file:
	
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

	# Extract Raw Audio from Wav File
	signal = file.readframes(-1)
	signal = np.fromstring(signal, "Int16")
	fs = file.getframerate()

#	for i in range(0, info[3]):
#		aux = file.readframes(1)
#		print(str(aux))
		
		#print('aux: ' + str(aux) + ' [4:6]: ' + str(aux[4:6]) + 'hex: ' + str(int(aux[4:6], 16)))
		#left.append(int(aux[4:6], 16))
		#right.append(int(aux[4:6], 16))
#	plt.plot(left, frames)
#	plt.plot(right, frames)



	Time = np.linspace(0, len(signal) / fs, num=len(signal))
	
	plt.figure(1)
	plt.title("Signal Wave...")
	plt.plot(Time, signal)
	plt.show()