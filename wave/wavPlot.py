import matplotlib.pyplot as plt
import numpy as np
import wavio

# Open wav file
file = 'azi_90,0_ele_0,0' # without extension
HRIR = wavio.read(file + ".wav") 

# Plot HRIR
sampling_time = np.arange(HRIR.data.shape[0])/HRIR.rate
plt.plot(sampling_time, HRIR.data[:,0], label="left")
plt.plot(sampling_time, HRIR.data[:,1], label="right")
plt.xlabel('time [s]')
plt.ylabel('HRIR')
plt.grid()
plt.legend()
plt.savefig("HRIR_" + file + ".png")
plt.close()