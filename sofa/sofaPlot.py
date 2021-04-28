
import numpy as np
from scipy.fft import fft, fftshift, fftfreq
import matplotlib.pyplot as plt
from matplotlib import ticker, cm
from pysofaconventions import *

# path = input("Introduce file's path (filename included): ")
sofa = SOFAFile('D1_48K_24bit_256tap_FIR_SOFA.sofa', 'r')
sampling_freq = sofa.getSamplingRate().data[0]  # 48 kHz
sampling_dt = 1/sampling_freq

print("SOFA Convention:", sofa.getGlobalAttributeValue('SOFAConventions'))
print("\n")
print("Dimensions:")
sofa.printSOFADimensions()

print("\n")
print("Variables")
sofa.printSOFAVariables()

# Get positions and HRIR data
# Source position contains:
# 1st coefficient in sourcePositions = azimuth angle [0,360]
# 2nd coefficient in sourcePositions = elevation angle [-90, 90]
# 3rd coefficient in sourcePositions = radial distance
# REMARK:
# Azimuth is measured anti-clockwise (to the left) about the horizontal plane.
# 0° marks directly in front of the subject.
# Elevation is measured above (positive) and below (negative) the horizontal plane.
# Measurements are labeled by azimuth and elevation in degrees accurate to 1 decimal place
sourcePositions = sofa.getVariableValue('SourcePosition')
data = sofa.getDataIR()

# Slice the data using only those measurements with a fixed angle (azimuth or elevation)
def plot_1D(sofa, sampling_dt, sourcePositions, data, azimuth, elevation, tol):

	# Get the data
	for m in range(sofa.getDimensionSize('M')):
		pto = sourcePositions[m].data
		if np.abs(pto[0] - azimuth) < tol and np.abs(pto[1] - elevation) < tol:
			data_HRIR_left=data[m, 0, :]
			data_HRIR_right=data[m, 1, :]
			break
	# Plot HRIR
	sampling_time = np.arange(sofa.getDimensionSize('N'))*sampling_dt
	plt.plot(sampling_time, data_HRIR_left, label="left")
	plt.plot(sampling_time, data_HRIR_right, label="right")
	plt.xlabel('time [s]')
	plt.ylabel('HRIR')
	plt.grid()
	plt.legend()
	plt.savefig("HRIR_azimuth="+str(azimuth)+"_elevation="+str(elevation)+".png")
	plt.close()

	# Compute HRTR functions
	data_HRTF_left = np.log(np.abs(fftshift(fft(data_HRIR_left))))
	data_HRTF_right = np.log(np.abs(fftshift(fft(data_HRIR_right))))
	# Compute frequency values
	freq = fftshift(fftfreq(sofa.getDimensionSize('N'), d=sampling_dt))
	# Plot HRTF
	plt.plot(freq, data_HRTF_left, label="left")
	plt.plot(freq, data_HRTF_right, label="right")
	plt.xlim((0,freq[-1]))
	plt.xlabel('frequency [Hz]')
	plt.ylabel('HRTF')
	plt.grid()
	plt.legend()
	plt.savefig("HRTF_azimuth="+str(azimuth)+"_elevation="+str(elevation)+".png")
	plt.close()

# Slice the data using only those measurements with a fixed angle (azimuth or elevation)
def plot_slice2D(sofa, sampling_dt, sourcePositions, data, angle, angle_fix, tol):
	if angle_fix == 'azimuth':
		pos_fix = 0; pos_swe = 1; angle_swe = 'elevation'
	else:
		pos_fix = 1; pos_swe = 0; angle_swe = 'azimuth'
	
	data_HRIR_left = []
	data_HRIR_right = []
	angle_HRIR = []
	for m in range(sofa.getDimensionSize('M')):
		pto = sourcePositions[m].data
		if np.abs(pto[pos_fix] - angle) < tol:
			angle_HRIR.append(pto[pos_swe])
			data_HRIR_left.append(data[m, 0, :])
			data_HRIR_right.append(data[m, 1, :])
	
	# Convert to numpy arrayelevation_HRIR = np.array(elevation_HRIR)
	angle_HRIR = np.array(angle_HRIR)
	data_HRIR_left = np.array(data_HRIR_left)
	data_HRIR_right = np.array(data_HRIR_right)
	sampling_time = np.arange(sofa.getDimensionSize('N'))*sampling_dt

	# Compute HRTR functions
	data_HRTF_left = np.zeros(data_HRIR_left.shape)
	data_HRTF_right = np.zeros(data_HRIR_right.shape)
	for j in range(data_HRIR_left.shape[0]):
		data_HRTF_left[j,:] = np.log(np.abs(fftshift(fft(data_HRIR_left[j,:]))))
		data_HRTF_right[j,:] = np.log(np.abs(fftshift(fft(data_HRIR_right[j,:]))))
	# Compute frequency values
	freq = fftshift(fftfreq(sofa.getDimensionSize('N'), d=sampling_dt))

	# Plot with respect to angle (left HRIR) 
	T, ANG = np.meshgrid(sampling_time, angle_HRIR)
	plt.figure()
	plt.contourf(ANG, T, data_HRIR_left, levels = 50, cmap=cm.bone)
	plt.ylim((sampling_time[0], sampling_time[-1]))
	plt.xlim((angle_HRIR.min(), angle_HRIR.max()))
	plt.ylabel('time [s]')
	plt.xlabel(angle_swe+' angle [degree]')
	plt.colorbar()
	plt.savefig("HRIR_left_"+angle_fix+"="+str(angle)+".png")
	plt.close()
	
	# Plot with respect to angle (right HRIR)
	plt.figure()
	plt.contourf(ANG, T, data_HRIR_right, levels = 50, cmap=cm.bone)
	plt.ylim((sampling_time[0], sampling_time[-1]))
	plt.xlim((angle_HRIR.min(), angle_HRIR.max()))
	plt.ylabel('time [s]')
	plt.xlabel(angle_swe+' angle [degree]')
	plt.colorbar()
	plt.savefig("HRIR_right_"+angle_fix+"="+str(angle)+".png")
	plt.close()

	# Plot with respect to angle (left HRTF) 
	F, ANG = np.meshgrid(freq, angle_HRIR)
	plt.figure()
	plt.contourf(ANG, F, data_HRTF_left, levels = 50, cmap=cm.bone)
	plt.ylim((0, freq[-1]))
	plt.xlim((angle_HRIR.min(), angle_HRIR.max()))
	plt.ylabel('frequency [Hz]')
	plt.xlabel(angle_swe+' angle [degree]')
	plt.colorbar()
	plt.savefig("HRTF_left_"+angle_fix+"="+str(angle)+".png")
	plt.close()
	
	# Plot with respect to angle (right HRTF) 
	F, ANG = np.meshgrid(freq, angle_HRIR)
	plt.figure()
	plt.contourf(ANG, F, data_HRTF_right, levels = 50, cmap=cm.bone)
	plt.ylim((0, freq[-1]))
	plt.xlim((angle_HRIR.min(), angle_HRIR.max()))
	plt.ylabel('frequency [Hz]')
	plt.xlabel(angle_swe+' angle [degree]')
	plt.colorbar()
	plt.savefig("HRTF_right_"+angle_fix+"="+str(angle)+".png")
	plt.close()

# Slice the data using only those measurements with azimuth = angle = 90 (left hand)
angle = 90; angle_fix = 'azimuth'; tol = 0.1
plot_slice2D(sofa, sampling_dt, sourcePositions, data, angle, angle_fix, tol)

# Slice the data using only those measurements with elevation = 0 (horizontal plane)
angle = 0; angle_fix = 'elevation'; tol = 0.1
plot_slice2D(sofa, sampling_dt, sourcePositions, data, angle, angle_fix, tol)

# Plot 1D
azimuth = 90; elevation = 0; tol = 0.1
plot_1D(sofa, sampling_dt, sourcePositions, data, azimuth, elevation, tol)