import matplotlib.pyplot as plt

# Sample data
pout_values = [0,6,30,45,60]
t20 = [30, 32,40, 67, 100 ]
t30 = [30, 35, 50, 60.3, 95 ]
t40 = [30, 32, 52, 57, 90]


# Create a figure and axis
fig, ax = plt.subplots()

# Plot the first set of values
ax.plot(pout_values, t20, label='Vin=20V', marker='o')
ax.plot(pout_values, t30, label='Vin=30V', marker='x')
ax.plot(pout_values, t40, label='Vin=40V', marker='*')

# Plot the second set of values
#ax.plot(x_values, values2, label='Values 2', marker='x')

# Adding labels and title
ax.set_xlabel('Output Power (W)')
ax.set_ylabel('Max Component Temperature (C)')
ax.set_title('Max component temperature when the output voltage reference is set to 12.5V')

# Adding legend
ax.legend()

# Adding grid
ax.grid(True)

# Display the plot
plt.show()