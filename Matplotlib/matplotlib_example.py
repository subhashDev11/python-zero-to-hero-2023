import matplotlib.pyplot as plt

#Line Plot
# Create some data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create the plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('X axis label')
plt.ylabel('Y axis label')
plt.title('Line Plot')

# Display the plot
plt.show()


#Scatter Plot:
# Create some data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create the plot
plt.scatter(x, y)

# Add labels and title
plt.xlabel('X axis label')
plt.ylabel('Y axis label')
plt.title('Scatter Plot')

# Display the plot
plt.show()

#Histogram 
import numpy as np

# Create some data
data = np.random.randn(1000)

# Create the plot
plt.hist(data, bins=30)

# Add labels and title
plt.xlabel('Data')
plt.ylabel('Frequency')
plt.title('Histogram')

# Display the plot
plt.show()
