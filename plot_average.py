import re
import matplotlib.pyplot as plt

def extract_data(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    step_numbers = [int(step) for step in re.findall(r'At step (\d+)', content)]
    average_returns = [float(avg_return) for avg_return in re.findall(r'Average return: \[([-+]?\d*\.\d+|\d+)\]', content)]

    return step_numbers, average_returns

# File paths for SAC and TD3
file_path1 = 'runs-txt/sac/sac-2023-12-11_22-09-15.txt'
file_path2 = 'runs-txt/sac/sac-2023-12-11_23-01-12.txt'
file_path3 = 'runs-txt/sac/sac-2023-12-11_23-14-18.txt'
file_path4 = 'runs-txt/sac/sac-2023-12-12_00-12-32.txt'
file_path5 = 'runs-txt/sac/sac-2023-12-12_02-34-13.txt'
file_path6 = 'runs-txt/sac/sac.txt'

# Extract data from files
steps1, returns1 = extract_data(file_path1)
steps2, returns2 = extract_data(file_path2)
steps3, returns3 = extract_data(file_path3)
steps4, returns4 = extract_data(file_path4)
steps5, returns5 = extract_data(file_path5)
steps6, returns6 = extract_data(file_path6)


all_returns = [returns1, returns2, returns3, returns4, returns5, returns6]

# Calculate the sum of corresponding elements across all lists
sum_returns = [sum(values) for values in zip(*all_returns)]

# Calculate the average by dividing the sum by the total number of lists
num_returns = len(all_returns)
average_returns = [value / num_returns for value in sum_returns]

# Plotting
plt.plot(steps1, average_returns, marker='o')

plt.title('Average Return vs Number of Steps')
plt.xlabel('Number of Steps')
plt.ylabel('Average Return')
plt.legend()
plt.grid(True)
plt.show()