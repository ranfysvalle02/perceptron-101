# Step 1: Define the input vector (student's scores)  
inputs = [85, 90]  # Test 1 score: 85, Test 2 score: 90  
  
# Step 2: Initialize weights (importance of each test)  
weights = [0.4, 0.6]  # Weight for Test 1: 0.4, Test 2: 0.6  
  
# Step 3: Define the bias (adjusts the passing threshold)  
bias = -80  # This scalar shifts the decision point  
  
# Step 4: Calculate the weighted sum  
weighted_sum = inputs[0]*weights[0] + inputs[1]*weights[1] + bias  
# Alternatively, use the dot product:  
#weighted_sum = sum(i * w for i, w in zip(inputs, weights)) + bias  
  
# Step 5: Define the activation function  
def activation_function(x):  
    if x >= 0:  
        return 1  # Pass  
    else:  
        return 0  # Fail  
  
# Step 6: Get the perceptron output  
output = activation_function(weighted_sum)  
  
# Step 7: Display the result  
if output == 1:  
    print("The student has passed.")  
else:  
    print("The student has failed.")  
