import re

with open('input.txt', 'r') as file:
    input = file.read()

# task 1
def find_all_matches(input):
    matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input)
    sum_of_matches = 0

    for pair in matches:
        pair_sum = int(pair[0]) * int(pair[1])
        sum_of_matches += pair_sum

    print(sum_of_matches)

find_all_matches(input)

# task 2
def find_enabling_matches(input):
    sum_of_matches = 0
    all_matches = re.findall(r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))", input)
    is_enabled = True 

    for match in all_matches:
        if match[0] == "do()":
            is_enabled = True
        elif match[0] == "don't()":
            is_enabled = False
        elif match[1] and is_enabled:
            sum_of_matches += int(match[1]) * int(match[2])
    
    print(sum_of_matches)

find_enabling_matches(input)

