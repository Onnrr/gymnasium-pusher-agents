import re
import matplotlib.pyplot as plt

def extract_data(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    step_numbers = [int(step) for step in re.findall(r'At step (\d+)', content)]
    average_returns = [float(avg_return) for avg_return in re.findall(r'Average return: \[([-+]?\d*\.\d+|\d+)\]', content)]

    return step_numbers, average_returns

# File paths for SAC and TD3
file_path1 = 'runs-txt/sac_her/sac-her-2023-12-12_17-23-39.txt'
file_path2 = 'runs-txt/sac_her/sac-her-2023-12-12_17-24-21.txt'
file_path3 = 'runs-txt/sac_her/sac-her-2023-12-12_17-24-29.txt'
file_path4 = 'runs-txt/sac_her/sac-her-2023-12-12_19-07-53.txt'
file_path5 = 'runs-txt/sac_her/sac-her-2023-12-12_19-08-01.txt'
file_path6 = 'runs-txt/sac_her/sac-her-2023-12-12_19-08-09.txt'

# Extract data from files
steps1, returns1 = extract_data(file_path1)
steps2, returns2 = extract_data(file_path2)
steps3, returns3 = extract_data(file_path3)
steps4, returns4 = extract_data(file_path4)
steps5, returns5 = extract_data(file_path5)
steps6, returns6 = extract_data(file_path6)


# Plotting
plt.plot(steps1, returns1, marker='o')
plt.plot(steps2, returns2, marker='o')
plt.plot(steps3, returns3, marker='o')
plt.plot(steps4, returns4, marker='o')
plt.plot(steps5, returns5, marker='o')
plt.plot(steps6, returns6, marker='o')

plt.title('Average Return vs Number of Steps')
plt.xlabel('Number of Steps')
plt.ylabel('Average Return')
plt.legend()
plt.grid(True)
plt.show()