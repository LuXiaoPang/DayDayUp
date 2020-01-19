#!/bin/python3
#=============================================================================
# Author          : luzhanzhao
# Email           : zhanzhao.lu@sina.com
# Last modified   : 2019-08-23 19:39
# Filename        : numpy_creat.py
# Description     : 
#=============================================================================
import numpy as np
#np.array(object, dtype=none, copy=True, order=None, subok=False, ndmin=0)
a = np.array([1,2,3,4])
print(a)
print(type(a))
#-> [1 2 3 4]
#-> a.data     is  <memory at 0x7f72918183a8>
#-> <class 'numpy.ndarray'>

a = np.array([1,2,3,4],dtype=complex)
print(a)
#-> [1.+0.j 2.+0.j 3.+0.j 4.+0.j]

a = np.array([1,2,3,4],ndmin=2)
print(a)
#-> [[1 2 3 4]]

print('a.ndim     is ',a.ndim     )
print('a.shape    is ',a.shape    )
print('a.size     is ',a.size     )
print('a.dtype    is ',a.dtype    )
print('a.itemsize is ',a.itemsize )
print('a.data     is ',a.data     )
#-> a.ndim     is  2
#-> a.shape    is  (1, 4)
#-> a.size     is  4
#-> a.dtype    is  int64
#-> a.itemsize is  8
#-> a.data     is  <memory at 0x7f011df6c2d0>

a = np.array([(1,2,3),(4,5)]) #will creat 1-D array
print(a)
#-> [(1, 2, 3) (4, 5)]

a = np.array([(1,2,3),(4,5,6)]) #will creat 2-D array
print(a)
#-> [[1 2 3]
#->  [4 5 6]]

a = np.zeros((3,4))
print(a)
#-> [[0. 0. 0. 0.]
#->  [0. 0. 0. 0.]
#->  [0. 0. 0. 0.]]

a = np.ones((3,4))
print(a)
#-> [[1. 1. 1. 1.]
#->  [1. 1. 1. 1.]
#->  [1. 1. 1. 1.]]

a = np.empty((3,4))
print(a)

a = np.arange(8)
print(a)
#-> [0 1 2 3 4 5 6 7]

a = np.arange(5,25,3)
print(a)
#-> [ 5  8 11 14 17 20 23]
