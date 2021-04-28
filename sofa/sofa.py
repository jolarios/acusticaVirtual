from pysofaconventions import *
import matplotlib.pyplot as plt
import scipy.signal
import soundfile as sf
import numpy as np


#path = input("Introduce file's path (filename included): ")
sofa = SOFAFile('proba1.sofa', 'r')
print("\n")

if(sofa.isValid()):
	print("SOFA Convention:", sofa.getGlobalAttributeValue('SOFAConventions'))
	print("\n")
	print("Dimensions:")
	sofa.printSOFADimensions()

	print("\n")
	print("Variables")
	sofa.printSOFAVariables()

	sourcePositions = sofa.getVariableValue('SourcePosition')
	

	m = 0
	print("\n")
	print("Source Position of measurement " + str(m))
	print(sourcePositions[m])
	
	data = sofa.getDataIR()
	hrtf = data[m,:,:]
	

	print("\n")
	print("HRTF dimensions")
	print(hrtf.shape)

	plt.plot(hrtf[0], label="left", linewidth=0.5,  marker='o', markersize=1)
	plt.plot(hrtf[1], label="right", linewidth=0.5,  marker='o', markersize=1)
	plt.grid()
	plt.legend()
	plt.show()

else:
	print("ERROR: SOFA file ", path, " is not valid!!")



#	dim_size = int(str(sofa.getDimension('M'))[-4:])
#	i = j = z = 0
#	inicial = sourcePositions[0, 0]
#	angulos = 1
#	azimuth = 0
#	contador = 0
#	max_azimuth = 0
#	for i in range(0,dim_size-1):
#		print("i = " + str(i) + " sourcePositions: " +str(sourcePositions[i,0]) + " inicial = "+str(inicial))
#		if inicial == sourcePositions[i, 0]:
#			contador = contador + 1
#		else:
#			if contador > max_azimuth:
#				max_azimuth = contador
#			inicial = sourcePositions[i,0]
#			angulos = angulos + 1
#			contador = 1
#	while i < dim_size:
#		#print("i = " + str(i) + "\nz =" + str(z) + "\nj = " + str(j) + "\n\n")
#		if x == int(sourcePositions[i, 0]):
#			mat[j][z] = sourcePositions[i]
#			++z
#		else:
#			x = int(sourcePositions[i, 0])
#			z = 0
#			++j
#		++i
