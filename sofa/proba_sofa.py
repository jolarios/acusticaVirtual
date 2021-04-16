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
