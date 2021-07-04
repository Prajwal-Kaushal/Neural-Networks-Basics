'''
Here we build our basic neural network by adding for loops to scale and 
handle dynamically sized inputs and layers.
'''

inputs = [1,2,3,2.5]

weights = [[0.2,0.8,-0.5,1],
           [0.5,-0.91,0.26,-0.5],
           [-0.26,-0.27,0.17,0.87]]
biases = [2, 3, 0.5]

#output of current layer
layer_output = []

#for each neuron
for neuron_weights, neuron_bias in zip(weights, biases):
    output = 0
    # For each input and weight to the neuron
    for wt, ip in zip(neuron_weights, inputs):
        # Multiply this input by associated weight
        # and add to the neuron's output variable
        output += wt * ip
    # Add bias
    output += neuron_bias
    # Put neuron's result to the layer's output list
    layer_output.append(output)
    
print(layer_output)
    
