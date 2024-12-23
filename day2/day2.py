with open('input.txt', 'r') as file:
    input = file.read()

lines = input.strip().splitlines()

reports = [list(map(int, line.split())) for line in lines]

# task 1a
def is_safe_report(report):
    total_difference = []
    absolute_difference = []

    for current, next_item in zip(report, report[1:]):
        difference = next_item - current
        total_difference.append(difference)
        absolute_difference.append(abs(difference))

        # if all(diff > 0 for diff in total_difference) or all(diff < 0 for diff in total_difference):
        #     print(f"{total_difference} is positive or negative")
        #     if all(1 <= i <= 3 for i in absolute_difference):
        #         safe_reports.append(report)
    
    is_consistent = all(diff > 0 for diff in total_difference) or all(diff < 0 for diff in total_difference)

    is_within_range = all(1 <= i <= 3 for i in absolute_difference)

    # report is safe if both conditions are true
    return is_consistent and is_within_range

# task 1b
def is_safe_with_dampener(report):
    # if the report is safe without modifications
    if is_safe_report(report):
        return True

    # if not, remove each level one at a time
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe_report(modified_report):
            return True 
        
    return False


# task 1a
safe_reports_task1a = [report for report in reports if is_safe_report(report)]
print(f"Task 1a: Number of safe reports: {len(safe_reports_task1a)}")

# task 1b
safe_reports_task1b = [report for report in reports if is_safe_with_dampener(report)]
print(f"Task 1b: Number of safe reports: {len(safe_reports_task1b)}")
