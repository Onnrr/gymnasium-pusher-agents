import re
import matplotlib.pyplot as plt

def extract_data(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    step_numbers = [int(step) for step in re.findall(r'At step (\d+)', content)]
    average_returns = [float(avg_return) for avg_return in re.findall(r'Average return: \[([-+]?\d*\.\d+|\d+)\]', content)]

    return step_numbers, average_returns

# File paths for SAC and TD3
sac_file_path = 'runs-txt/td/td.txt'
sac_file_path2 = 'runs-txt/td_different_gamma/td-2023-12-13_01-57-21.txt'
sac_file_path3 = 'runs-txt/td_different_gamma/td-2023-12-13_01-57-17.txt'

# Extract data from files
sac_steps, sac_returns = extract_data(sac_file_path)
sac_steps2, sac_returns2 = extract_data(sac_file_path2)
sac_steps3, sac_returns3 = extract_data(sac_file_path3)

# Plotting
plt.plot(sac_steps, sac_returns, label='0.99', marker='o')
plt.plot(sac_steps2, sac_returns2, label='0.90', marker='o')
plt.plot(sac_steps3, sac_returns3, label='0.80', marker='o')

plt.title('TD3 - Average Return vs Number of Steps for Different Discount Rates')
plt.xlabel('Number of Steps')
plt.ylabel('Average Return')
plt.legend()
plt.grid(True)
plt.show()