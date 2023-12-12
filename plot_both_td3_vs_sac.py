import re
import matplotlib.pyplot as plt

def extract_data(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    step_numbers = [int(step) for step in re.findall(r'At step (\d+)', content)]
    average_returns = [float(avg_return) for avg_return in re.findall(r'Average return: \[([-+]?\d*\.\d+|\d+)\]', content)]

    return step_numbers, average_returns


######################################## SAC #################################################
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


######################################## TD3 #################################################
file_path7 = 'runs-txt/td/td-2023-12-11_22-07-25.txt'
file_path8 = 'runs-txt/td/td-2023-12-11_22-32-52.txt'
file_path9 = 'runs-txt/td/td-2023-12-11_23-02-44.txt'
file_path10 = 'runs-txt/td/td-2023-12-11_23-51-26.txt'
file_path11 = 'runs-txt/td/td-2023-12-12_00-01-01.txt'
file_path12 = 'runs-txt/td/td.txt'


# Extract data from files
steps7, returns7 = extract_data(file_path7)
steps8, returns8 = extract_data(file_path8)
steps9, returns9 = extract_data(file_path9)
steps10, returns10 = extract_data(file_path10)
steps11, returns11 = extract_data(file_path11)
steps12, returns12 = extract_data(file_path12)


all_returns1 = [returns7, returns8, returns9, returns10, returns11, returns12]

# Calculate the sum of corresponding elements across all lists
sum_returns1 = [sum(values) for values in zip(*all_returns1)]

# Calculate the average by dividing the sum by the total number of lists
num_returns1 = len(all_returns1)
average_returns1 = [value / num_returns1 for value in sum_returns1]

# Plotting
plt.plot(steps1, average_returns, label='SAC', marker='o')
plt.plot(steps7, average_returns1, label='TD3', marker='o')

plt.title('Average Return vs Number of Steps')
plt.xlabel('Number of Steps')
plt.ylabel('Average Return')
plt.legend()
plt.grid(True)
plt.show()