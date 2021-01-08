# 2018 Linear Algebra assignment 1

import numpy as np
import matplotlib.pyplot as plt

# create the probability matrix of the graph
A = np.array([[  0,   0,   0,   0,0.35,  0,    0,     0,     0,     0,   0,    0,    0,   0],
             [0.17,   0,   0,   0,   0,0.6,    0,     0,     0,     0,   0,    0,    0,   0],
             [0.13,   0,   0,   0,   0,  0,    0,     0,     0,     0,   0,    0,    0,   0],
             [ 0.2,   0,   0,   0,   0,  0,2.0/3,     0,     0,     0,   0,    0,    0,   0],
             [   0,   0,   0,0.89,   0,0.4,    0,     0, 2.0/3, 1.0/3,   0,    0,    0,   0],
             [ 0.4,   0,   0,0.11,   0,  0,    0,     0,     0,     0,   0,    0,    0,   0],
             [   0,   0,   0,   0,   0,  0,    0,     0,     0,     0, 1.0,    0,    0,   0],
             [   0,   0,   0,   0,   0,  0,    0,     0,     0, 2.0/3,   0,    0,    0,   0],
             [   0, 0.5,0.58,   0,   0,  0,    0,     0,     0,     0,   0,    0,    0,   0],
             [   0,   0,0.42,   0,   0,  0,    0,     0,     0,     0,   0,    0,    0,0.62],
             [   0, 0.5,   0,   0,   0,  0,    0,   0.5,     0,     0,   0,    0, 0.24,0.38],
             [   0,   0,   0,   0,   0,  0,    0,     0,     0,     0,   0,    0,    0,   0],
             [   0,   0,   0,   0,0.65,  0,    0,     0, 1.0/3,     0,   0, 0.85,    0,   0],
             [ 0.1,   0,   0,   0,   0,  0,1.0/3,   0.5,     0,     0,   0, 0.15, 0.76,   0]])

# create an initial zero vector
v0 = np.zeros([14,1])

# define a function to compute |a-b|
#------------------------------------------------
def abssum(a, b):
    """this function computes the norm of a-b"""
    result = 0
    for i in range(len(a)):
        result = result + abs(a[i]-b[i])
    return result[0]
#------------------------------------------------
def vecsum(a):
    result = 0
    for i in range(len(a)):
        result = result +a[i]
    return result[0]

plt.figure
for j in range(14):
    v=v0
    if(j!=0):
        v[j-1]=[0]
    v[j] = [1]
    #print(v)
    # compute their product
    u = np.dot(A, v)
    # diff records the difference of Av and v
    diff = [abssum(u,v)]
    i = 0
    while diff[i] > 1e-5:
        v = u            # record A^kv
        u = np.dot(A, v)  # compute A^{k+1}v
        diff.append(abssum(u, v))  # append add
        i = i + 1
        print(vecsum(u))

    #plot the differences with iterations
    #plt.subplot(7,2,j+1)
    plt.semilogy(range(len(diff)), diff,label='vector '+str(j))
plt.xlabel('iterations')
plt.ylabel('difference')
plt.title('Convergence')
plt.legend()
plt.show()


