import matplotlib.pyplot as plt

# Sample data
pout_values = [0,6,30,45,60]
v20 = [12.5, 12.46, 12.4, 12.3, 12.2]
v30 = [12.5, 12.46, 12.4, 12.4, 12.2]
v40 = [12.5,12.48, 12.5,12.4, 12.2]


# Create a figure and axis
fig, ax = plt.subplots()

# Plot the first set of values
ax.plot(pout_values, v20, label='Vin=20V', marker='o')
ax.plot(pout_values, v30, label='Vin=30V', marker='x')
ax.plot(pout_values, v40, label='Vin=40V', marker='*')

# Plot the second set of values
#ax.plot(x_values, values2, label='Values 2', marker='x')

# Adding labels and title
ax.set_xlabel('Output Power (W)')
ax.set_ylabel('Output Voltage (V)')
ax.set_title('Voltage regulation when output voltage reference is set to 12.5V')

# Adding legend
ax.legend()

# Adding grid
ax.grid(True)

# Display the plot
plt.show()