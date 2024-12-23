with open('input.txt', 'r') as file:
    input = file.read()

lines = input.strip().splitlines()
left = []
right = []

for numbers in lines:
    l, r = map(int, numbers.split())  
    left.append(l)  
    right.append(r)

left.sort()
right.sort()

#task 1a
absolute_difference = 0

for num in range(len(left)):
    difference = abs(right[num] - left[num])
    absolute_difference += difference

#print(absolute_difference)

#task 1b
left_count = {}
for num in left:
    if num in left_count:
        left_count[num] += 1 
    else:
        left_count[num] = 1

similarity_score = 0
for num in right:
    occurrences = left_count.get(num, 0)  
    similarity_score += num * occurrences

print(similarity_score)
