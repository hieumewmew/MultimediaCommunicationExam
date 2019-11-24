import numpy as np
import scipy
from scipy import signal

K = 10
X = np.random.randint(K, size=8)
Y = np.random.randint(K, size=4)
# X = np.array([1,0,0,1,8,2])
# Y = np.array([1,0,1])
print('X = ', X)
print('Y = ', Y)

def linear_Conv(X, Y):
    print('linear convolution:')

    n = np.shape(X)[0]
    m = np.shape(Y)[0]

    # swap [y(0), y(1),...,y(m-1)] -> [y(m-1), y(m-2),...,y(0)]
    Y_swap = np.array([Y[m-1-i] for i in range(m)])

    # padding 0 to left and right of Y_swap( len(Y_pad) = 2*(n-1)+m)
    Y_pad = np.pad(Y_swap, (n-1,n-1), 'constant', constant_values=(0,0))
    #print('Y_pad = ', Y_pad)

    matrix_Y = np.array([Y_pad[(n-1)+m-i-1 : 2*(n-1)+m-i] for i in range(m+n-1)])
    #print('matrix_Y :\n', matrix_Y)

    matrix_X = X.T
    #print('matrix_X :', matrix_X)

    matrix_Z = np.dot(matrix_Y, matrix_X)
    print('matrix_Z : ', matrix_Z)

    Z = np.sum(matrix_Z, axis=0)
    return Z

def cyclic_Conv(X, Y):
    #print('cyclic convolution :')

    n = np.shape(X)[0]
    m = np.shape(Y)[0]

     # swap [y(0), y(1),...,y(m-1)] -> [y(m-1), y(m-2),...,y(0)]
    Y_swap = np.array([Y[m-1-i] for i in range(m)])

    # padding 0 to left of Y_swap (len(Y_pad = n))
    Y_pad = np.pad(Y_swap, (n-m,0), 'constant', constant_values=(0,0))
    Y_double = np.concatenate((Y_pad, Y_pad), axis=0)
    #print('Y_double = ', Y_double)

    matrix_X = X.T
    #print('matrix_X = ', matrix_X)

    matrix_Y = np.array([ Y_double[n-1-i : 2*n-1-i] for i in range(n)])
    #print('matrix_Y :\n ', matrix_Y)

    matrix_Z = np.dot(matrix_Y, matrix_X)
    print('matrix_Z = ', matrix_Z)

    Z = np.sum(matrix_Z, axis=0)
    return Z

print('linear convolution', linear_Conv(X, Y))    
print('cyclic convolution', cyclic_Conv(X, Y))
linear_convolve_csipy = signal.convolve(X, Y, mode='full', method='direct')
print('linear convolve csipy: ', linear_convolve_csipy)

# scipy don't have function to calculate directly cyclic convolution