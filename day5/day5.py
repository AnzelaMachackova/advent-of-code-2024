# input = """
#     47|53
#     97|13
#     97|61
#     97|47
#     75|29
#     61|13
#     75|53
#     29|13
#     97|29
#     53|29
#     61|53
#     97|53
#     61|29
#     47|13
#     75|47
#     97|75
#     47|61
#     75|61
#     47|29
#     75|13
#     53|13

#     75,47,61,53,29
#     97,61,53,29,13
#     75,29,13
#     75,97,47,61,53
#     61,13,29
#     97,13,75,29,47
# """


with open('input.txt', 'r') as file:
    input = file.read()

def parse_input(input_str):
    lines = input_str.strip().split('\n')
    
    pairs_dict = []
    lists = []

    processing_pairs = True
    
    for line in lines:
        line = line.strip()
        if not line:
            processing_pairs = False
            continue
        
        if processing_pairs:
            key, value = map(int, line.split('|'))
            pairs_dict.append((key, value))
        else:
            lists.append(list(map(int, line.split(','))))
    
    return pairs_dict, lists

pairs_rules, pages = parse_input(input)

# pairs_rules = {47: 29, 97: 75, 75: 13, 61: 29, 29: 13, 53: 13}
# pages = [[75, 47, 61, 53, 29], [97, 61, 53, 29, 13], [75, 29, 13], [75, 97, 47, 61, 53], [61, 13, 29], [97, 13, 75, 29, 47]]

def filter_rules_for_update(update, pairs_rules):
    relevant_rules = []

    for x, y in pairs_rules:
        if x in update and y in update:
            relevant_rules.append((x, y)) 
    return relevant_rules

def is_update_valid(update, relevant_rules):
    for x, y in relevant_rules:
        if update.index(x) >= update.index(y): 
            return False
    return True

total_middle_sum = 0

for update in pages:
    relevant_rules = filter_rules_for_update(update, pairs_rules)
    #print(relevant_rules)

    if is_update_valid(update, relevant_rules):
        middle_page = update[len(update) // 2]
        total_middle_sum += middle_page

print(f"Total sum of middle pages: {total_middle_sum}")