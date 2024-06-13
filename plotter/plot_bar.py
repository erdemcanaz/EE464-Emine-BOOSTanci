import matplotlib.pyplot as plt

# Sample data
x = ['Pin', 'Pout', 'Psnubber', 'Poutput_diode', 'Pcore', 'Pmosfet',  'Pwinding', 'Pdiode_snubber','Pshunt', 'Pesr','Pother']
y = [74.95, 58.41, 2.53, 2.91, 2.59 , 0.92, 0.23, 0.16, 1.8, 3.3, 2.2]

x = [x for _, x in sorted(zip(y, x), reverse=True)]
y = sorted(y, reverse=True)

# Plotting the bar chart
plt.bar(x, y, color=['darkblue'] + ['lightblue'] * (len(x) - 1))
for i, v in enumerate(y):
    plt.text(i, v, f"{v:.1f}W - "+str(round((v / max(y)) * 100, 2)) + '%', ha='center', va='bottom')
#plt.xticks(rotation=90)

# Adding labels and title
plt.xlabel('Categories')
plt.ylabel('Power (W)')
plt.title('Power distribution in the converter')


# Displaying the chart
plt.show()