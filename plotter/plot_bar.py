import matplotlib.pyplot as plt

# Sample data
x = ['Pin', 'Pout', 'Psnubber', 'Poutput_diode', 'Pcore', 'Pmosfet',  'Pwinding', 'Pdiode_snubber','Pother']
y = [77.61, 62.782, 3.579, 3.33, 2.541, 2.389, 0.3, 0.21, 2.51]

# Plotting the bar chart
plt.bar(x, y)
for i, v in enumerate(y):
    plt.text(i, v, f"{v:.1f}W - "+str(round((v / max(y)) * 100, 2)) + '%', ha='center', va='bottom')
#plt.xticks(rotation=90)

# Adding labels and title
plt.xlabel('Categories')
plt.ylabel('Power (W)')
plt.title('Power distribution in the converter')


# Displaying the chart
plt.show()