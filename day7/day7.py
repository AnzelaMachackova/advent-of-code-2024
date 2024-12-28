with open('input.txt', 'r') as file:
    input = file.read()

def parse_input(input_data):
    lines = input_data.strip().splitlines()
    pairs_dict = {}
    for line in lines:
        key, *values = line.split(':')
        key = int(key.strip())
        values = list(map(int, values[0].strip().split()))
        pairs_dict[key] = values
    return pairs_dict

# recursive function to evaluate combinations
def evaluate_combinations(numbers, target):
    return explore_combinations(numbers, target, 1, numbers[0])

def explore_combinations(numbers, target, index, current_value):
    if index == len(numbers):
        return current_value == target

    # addition
    if explore_combinations(numbers, target, index + 1, current_value + numbers[index]):
        return True

    # multiplication
    if explore_combinations(numbers, target, index + 1, current_value * numbers[index]):
        return True

    return False

# main
def find_valid_calibration_sum(input_data):
    pairs_dict = parse_input(input_data)
    possible_configurations = []

    for key, value in pairs_dict.items():
        if evaluate_combinations(value, key):
            possible_configurations.append(key)

    return sum(possible_configurations), possible_configurations

result_sum, possible_configurations = find_valid_calibration_sum(input)
#print(f"Possible Configurations: {possible_configurations}")
print(f"Sum of Valid Test Values: {result_sum}")