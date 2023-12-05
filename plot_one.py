import re
import matplotlib.pyplot as plt

# Read the content of the txt file
with open('td.txt', 'r') as file:
    content = file.read()

# Use regular expressions to find step numbers and average returns
step_numbers = [int(step) for step in re.findall(r'At step (\d+)', content)]
average_returns = [float(avg_return) for avg_return in re.findall(r'Average return: \[([-+]?\d*\.\d+|\d+)\]', content)]

# Plotting
plt.plot(step_numbers, average_returns, marker='o', color="orange")
plt.title('Average Return vs Number of Steps')
plt.xlabel('Number of Steps')
plt.ylabel('Average Return')
plt.grid(True)
plt.show()