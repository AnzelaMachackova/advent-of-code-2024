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

# part 1
for update in pages:
    relevant_rules = filter_rules_for_update(update, pairs_rules)
    #print(relevant_rules)

    if is_update_valid(update, relevant_rules):
        middle_page = update[len(update) // 2]
        total_middle_sum += middle_page

print(f"Total sum of middle pages for part 1: {total_middle_sum}")

# part 2
incorrectly_ordered = []

for update in pages:
    relevant_rules = filter_rules_for_update(update, pairs_rules)
    if not is_update_valid(update, relevant_rules):
            incorrectly_ordered.append(update)

# print(incorrectly_ordered)

# 75,97,47,61,53 becomes 97,75,47,61,53.
# 61,13,29 becomes 61,29,13.
# 97,13,75,29,47 becomes 97,75,47,29,13.

def reorder_update(update, rules):
    changed = True

    while changed:
        changed = False
        for x, y in rules:
            if x in update and y in update:
                index_x = update.index(x)
                index_y = update.index(y)
                # print(index_x, index_y)
                if index_x > index_y:  
                    update.remove(x)
                    update.insert(index_y, x)
                    changed = True  
    # print(update)
    return update


fixed_updates = []
for update in incorrectly_ordered: 
    filtered_updates = filter_rules_for_update(update, pairs_rules)
    new_update = reorder_update(update, filtered_updates)
    fixed_updates.append(new_update)
# print(fixed_updates)
total_middle_sum = sum(update[len(update) // 2] for update in fixed_updates)
print(f"Total sum of middle pages for part 2: {total_middle_sum}")