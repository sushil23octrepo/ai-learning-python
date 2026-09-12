import numpy as np

# --------------------------------
# ONE SAMPLE + ONE NEURON
# --------------------------------

customer = np.array([0.72, 0.85, 0.25])

weights_one_neuron = np.array([0.40, 0.90, -0.70])


# 1D @ 1D performs a dot product
one_output = customer @ weights_one_neuron

print("One customer, one neuron:")
print(one_output)


# --------------------------------
# MULTIPLE SAMPLES + ONE NEURON
# --------------------------------

# Rows = customers/samples
# Columns = input features
customers = np.array([[0.72, 0.85, 0.25], [0.40, 0.55, 0.80], [0.91, 0.90, 0.10]])


# (3 samples, 3 features) @ (3 weights)
# Result = one output for each sample
outputs_one_neuron = customers @ weights_one_neuron

print("\nMultiple customers, one neuron:")
print(outputs_one_neuron)

print("Shape:")
print(outputs_one_neuron.shape)


# --------------------------------
# MULTIPLE SAMPLES + MULTIPLE NEURONS
# --------------------------------

# Rows = input features
# Columns = neurons
weights = np.array([[0.40, -0.20], [0.90, 0.50], [-0.70, 0.30]])


# Shape rule:
# (3 samples, 3 features) @ (3 features, 2 neurons)
# -> (3 samples, 2 neuron outputs)
outputs = customers @ weights

print("\nMultiple customers, multiple neurons:")
print(outputs)

print("Shape:")
print(outputs.shape)


# --------------------------------
# ADD BIAS
# --------------------------------

# One bias for each neuron/output column
biases = np.array([0.10, -0.05])


# Biases shape (2,) is broadcast across every customer row
layer_output = outputs + biases

print("\nLayer output with bias:")
print(layer_output)

print("Shape:")
print(layer_output.shape)


# --------------------------------
# COMPLETE LAYER IN ONE LINE
# --------------------------------

complete_layer_output = customers @ weights + biases

print("\nComplete layer calculation:")
print(complete_layer_output)


# --------------------------------
# * VS @
# --------------------------------

a = np.array([[1, 2], [3, 4]])

b = np.array([[5, 6], [7, 8]])


# * multiplies values at matching positions
element_wise = a * b

print("\nElement-wise multiplication:")
print(element_wise)


# @ performs matrix multiplication
matrix_product = a @ b

print("\nMatrix multiplication:")
print(matrix_product)
