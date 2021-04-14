from pysofaconventions import *
import matplotlib.pyplot as plt
import scipy.signal
import soundfile as sf
import numpy as np


path = input("Introduce file's path (filename included): ")
sofa = SOFAFile(path, 'r')
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
	dim_size = int(str(sofa.getDimension('M'))[-4:])
	i = j = z = 0
	mat = [[],[]]
	x = int(sourcePositions[0, 0])
'''
	while i < dim_size:
		print("i = " + str(i) + "\nz =" + str(z) + "\nj = " + str(j) + "\n\n")

		if x == int(sourcePositions[i, 0]):
			mat[j][z] = sourcePositions[i]
			++z
		else:
			x = int(sourcePositions[i, 0])
			z = 0
			++j
		++i
'''

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
