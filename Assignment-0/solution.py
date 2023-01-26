import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


alpha = 3
delta = -2
lam = 0.5
N = 10000
np.random.seed(0)

A = np.zeros(shape=(N, 3))
b = np.zeros(shape=(N, 1))

for i in range(N):

    x1 = np.random.normal(0,1)


    epsilon = np.random.uniform(-1, 1)
    x2 = alpha + (.2 * x1) + epsilon

    y = delta + (1.2 * x1) + np.random.exponential(lam)
    
    # Yi = delta + B1X1i + B2X2i
    A[i] = [delta, x1, x2]
    b[i] = [y]

# x = np.linalg.lstsq(b, A)

x = sm.OLS(b, A)
results = x.fit()
print(results.summary())

alpha = 3
delta = -2
lam = 0.5
N = 10000
num_estimates = 1000
np.random.seed(0)

coefficients = []
std_errs = []

for i in range(num_estimates):
    
    A = np.zeros(shape=(int(N/num_estimates), 3))
    b = np.zeros(shape=(int(N/num_estimates), 1))

    for i in range(int(N/num_estimates)):

        x1 = np.random.normal(0,1)


        epsilon = np.random.uniform(-1, 1)
        x2 = alpha + (.2 * x1) + epsilon

        y = delta + (1.2 * x1) + np.random.exponential(lam)
        
        # Yi = delta + B1X1i + B2X2i
        A[i] = [delta, x1, x2]
        b[i] = [y]

    x = sm.OLS(b, A)
    results = x.fit()

    coefficients.append(results.params)
    std_errs.append(results.HC3_se)



fig, axs = plt.subplots(ncols=3, nrows=1, figsize=(20, 6))



deltas = np.array([ d[0] for d in coefficients ])

axs[0].hist(deltas, bins=50)
axs[0].axvline(deltas.mean(), color='r')

axs[0].set_xlabel("Value")
axs[0].set_ylabel("Frequency")
axs[0].set_title("Delta")

Beta_1 = np.array([ b_1[1] for b_1 in coefficients ])

axs[1].hist(Beta_1, bins=50)
axs[1].axvline(Beta_1.mean(), color='r')
axs[1].set_xlabel("Value")
axs[1].set_ylabel("Frequency")
axs[1].set_title("Beta_1")

Beta_2 = np.array([ b_2[2] for b_2 in coefficients ])

axs[2].hist(Beta_2, bins=50)
axs[2].axvline(Beta_2.mean(), color='r')
axs[2].set_xlabel("Value")
axs[2].set_ylabel("Frequency")
axs[2].set_title("Beta_2")

fig.suptitle("Distributions of Coefficients")

plt.savefig("coefficient-distributions.png")

plt.show()
