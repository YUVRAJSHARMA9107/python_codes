import numpy as nd
array=nd.array([1,3,2,1,3])
print(array)
arr2=nd.array([[[1,2,3],[1,2,77]],[[1,2,3],[1,2,90]]])
print("the dimension is ",arr2.ndim)
print(arr2[1:-3:-1])