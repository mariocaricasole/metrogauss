import numpy as np
import matplotlib.pyplot as plt

vals = np.loadtxt("values.txt")

#evaluate mean and "normal" standard deviation
mean = np.mean(vals[5000:])
std = np.std(vals[5000:])

#define autocorrelation function
def C(k,sample):
    N=len(sample)
    product1 = sample[:N-k] - sample.mean()
    product2 = sample[k:] - sample.mean()

    return np.sum(product1*product2)/((N-k)*sample.std())

def tau(M,sample):
    N=len(sample)
    kk = np.linspace(1,M,M-1,dtype=int)

    CC = map(lambda x:C(x,sample),kk)
    CC=np.asarray(list(CC),dtype=np.float32)

    return CC.sum()

mm = np.linspace(1,len(vals)-1,int((len(vals)-2)/100),dtype=int)
TT = map(lambda x:tau(x,vals),mm)
TT = np.asarray(list(TT),dtype=np.float32)

plt.figure()
plt.plot(TT)
plt.show()
