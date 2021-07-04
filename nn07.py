'''
Now we have to add activation function to our code so that our model can fit to 
non linear data. There are many activation functions which we can use like:
    Step function
    Linear Activation
    Sigmoid
    ReLU - Rectified linear
Equations for the above can be seen on the internet.

We wont be using Step function because it is very simple and it doesn't provide much information.
We wont use Linear Activation because it is linear.
Sigmoid is good 
ReLU is good

For now we will be using ReLU bucause it is ALMOST same as Linear but it is non-linear
and it is simpler than Sigmoid.
'''
#%%
# ReLU activation function

# if input x >= 0 then output y = x
# if input x < 0 then output y = 0

inputs = [0, 1, -5, -100, 20]

output = []
for i in inputs:
    if i > 0:
        output.append(i)
    else:
        output.append(0)
print(output)

#%%

# We can make the same thing simpler 

import numpy as np

inputs = [0, 1, -5, -100, 20]

outputs = np.maximum(0, inputs)
print (outputs)