import re
import matplotlib.pyplot as plt

def extract_data(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    step_numbers = [int(step) for step in re.findall(r'At step (\d+)', content)]
    average_returns = [float(avg_return) for avg_return in re.findall(r'Average return: \[([-+]?\d*\.\d+|\d+)\]', content)]

    return step_numbers, average_returns

# File paths for SAC and TD3
sac_file_path = 'sac.txt'
td3_file_path = 'td.txt'

# Extract data from files
sac_steps, sac_returns = extract_data(sac_file_path)
td3_steps, td3_returns = extract_data(td3_file_path)

# Plotting
plt.plot(sac_steps, sac_returns, label='SAC', marker='o')
plt.plot(td3_steps, td3_returns, label='TD3', marker='o')

plt.title('Average Return vs Number of Steps')
plt.xlabel('Number of Steps')
plt.ylabel('Average Return')
plt.legend()
plt.grid(True)
plt.show()