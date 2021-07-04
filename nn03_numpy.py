'''
Now let's code with numpy
'''

# Single neuron with numpy

import numpy as np

inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0

outputs = np.dot(weights, inputs) + bias

print(outputs)
#%%
'''
Layer of neurons with numpy
'''

inputs = [1,2,3,2.5]

weights = [[0.2,0.8,-0.5,1],
           [0.5,-0.91,0.26,-0.5],
           [-0.26,-0.27,0.17,0.87]]
biases = [2, 3, 0.5]

layer_outputs = np.dot(weights, inputs) + biases

print(layer_outputs)

#%%

'''
Batch of inputs
Till now our input was vector and weight was either a vector or a matrix.
Now our input is also a matrix. So we will have to do matrix multiplication.

vector(a) . vector(b) = matrix(a) . Transpose(matrix(b))
'''

inputs = [[1.0, 2.0, 3.0, 2.5],
          [2.0, 5.0, -1.0, 2.0],
          [-1.5, 2.7, 3.3, -0.8]]

weights = [[0.2,0.8,-0.5,1],
           [0.5,-0.91,0.26,-0.5],
           [-0.26,-0.27,0.17,0.87]]

biases = [2, 3, 0.5]

outputs = np.dot(inputs, np.array(weights).T) + biases

print(outputs)
