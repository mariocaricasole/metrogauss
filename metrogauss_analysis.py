import numpy as np
import matplotlib.pyplot as plt

vals = np.loadtxt("values.txt")

#evaluate mean and "normal" standard deviation
mean = np.mean(vals[5000:])
std = np.std(vals[5000:])

#define autocorrelation function
def C(k,sample):
    N=len(sample)
    array = np.zeros_like(k,dtype=np.float64)
    for kk in k:
        product1 = sample[:N-kk] - sample.mean()
        product2 = sample[kk:] - sample.mean()
        out=np.sum(product1*product2)/((N-kk)*sample.std())
        array[kk-1] = out

    return array

#compute autocorrelation table up to M steps
def autocorr_table(M,sample):
    N=len(sample)
    kk = np.linspace(0,M,M,dtype=int)
    CC = C(kk,sample)

    return CC

#compute autocorrelation table for whole sample
table = autocorr_table(len(vals)-1,vals)

#define array of taus and fill it buy summing cumulatively (like integrating autocorrelation function)
tau = np.zeros_like(table)
tau[0]=table[0]
for i in range(0,len(tau)-1):
    tau[i+1] = tau[i] + table[i+1]

tau = np.asarray(tau)

#plot out
plt.figure()
plt.plot(tau)
plt.show()
