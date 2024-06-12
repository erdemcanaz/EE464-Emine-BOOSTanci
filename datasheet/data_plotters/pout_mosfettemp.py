import matplotlib.pyplot as plt

# Sample data
pout_values = [0,6,30,45,60]
tmos20 = [30, 26, 33, 55, 70 ]
tmos30 = [30, 28, 35, 45, 57 ]
tmos40 = [30, 27, 37, 40, 55]


# Create a figure and axis
fig, ax = plt.subplots()

# Plot the first set of values
ax.plot(pout_values, tmos20, label='Vin=20V', marker='o')
ax.plot(pout_values, tmos30, label='Vin=30V', marker='x')
ax.plot(pout_values, tmos40, label='Vin=40V', marker='*')

# Plot the second set of values
#ax.plot(x_values, values2, label='Values 2', marker='x')

# Adding labels and title
ax.set_xlabel('Output Power (W)')
ax.set_ylabel('Max Mosfet Temperature (C)')
ax.set_title('Max mosfet temperature when the output voltage reference is set to 12.5V')

# Adding legend
ax.legend()

# Adding grid
ax.grid(True)

# Display the plot
plt.show()