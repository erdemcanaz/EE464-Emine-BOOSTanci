import matplotlib.pyplot as plt

# Sample data
vin_values = [20,30,40]
vout_6 = [12.46, 12.48, 12.5]
vout_30 = [12.4, 12.4, 12.5]
vout_45 = [12.3, 12.4, 12.4]
vout_60 = [12.2,12.2,12.2]


# Create a figure and axis
fig, ax = plt.subplots()

# Plot the first set of values
ax.plot(vin_values, vout_6, label='Pout=6W', marker='o')
ax.plot(vin_values, vout_30, label='Pout=30W', marker='x')
ax.plot(vin_values, vout_45, label='Pout=45W', marker='*')
ax.plot(vin_values, vout_60, label='Pout=60W', marker='*')

# Plot the second set of values
#ax.plot(x_values, values2, label='Values 2', marker='x')

# Adding labels and title
ax.set_xlabel('Output Voltage (V)')
ax.set_ylabel('Input Voltage (V)')
ax.set_title('Line regulation when output voltage reference is set to 12.5V')

# Adding legend
ax.legend()

# Adding grid
ax.grid(True)

# Display the plot
plt.show()