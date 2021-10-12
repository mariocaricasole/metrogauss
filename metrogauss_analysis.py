import numpy as np
import matplotlib.pyplot as plt
from autocorr_time import autocorr_table, tau
import logging

vals = np.loadtxt("values.txt")

#evaluate mean and "normal" standard deviation
mean = np.mean(vals)
var = np.var(vals)

#compute autocorrelation table for whole sample
table = autocorr_table(len(vals)-1,vals)

#define array of taus and fill it buy summing cumulatively (like integrating autocorrelation function)
tau_arr = tau(vals)

#evaluate corrected variance
sigma_correct = var * (1+2*np.max(tau_arr))/len(vals)
print(f"Corrected variance: {sigma_correct}")

#plot out
plt.figure()
plt.plot(tau_arr)
plt.show()
