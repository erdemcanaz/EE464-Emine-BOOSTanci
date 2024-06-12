import matplotlib.pyplot as plt

# Sample data
pout_values = [0,6,30,45,60]
p20 = [3.6, 12.5, 46.2, 77, 99] #input power
p30 = [3.6, 13.1, 47.2, 69.5, 95.1]
p40= [3.6,13.5, 49.5, 75.5, 92.3]

e20 = [0, 48, 64.93, 58.44, 60.6 ]
e30 = [0, 45.8, 63.55, 64.74, 63.09 ]
e40 = [0, 44.4, 60.6, 59.6, 65.0]    

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the first set of values
# ax.plot(pout_values, p20, label='Vin=20V', marker='o')
# ax.plot(pout_values, p30, label='Vin=30V', marker='x')
# ax.plot(pout_values, p40, label='Vin=40V', marker='*')

# Plot the first set of values
ax.plot(pout_values, e20, label='Vin=20V', marker='o')
ax.plot(pout_values, e30, label='Vin=30V', marker='x')
ax.plot(pout_values, e40, label='Vin=40V', marker='*')
# Plot the second set of values
#ax.plot(x_values, values2, label='Values 2', marker='x')

# Adding labels and title
ax.set_xlabel('Output Power (W)')
ax.set_ylabel('Efficiency (%)')
ax.set_title('Efficiency and output power relation when output voltage reference is set to 12.5V')

# Adding legend
ax.legend()

# Adding grid
ax.grid(True)

# Display the plot
plt.show()