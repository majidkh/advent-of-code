import re
def check_increase_safe (data):
    is_valid = True
    current_num = data[0]
    for i in range(len(data) - 1):
        next_number = data[i + 1]

        if current_num > next_number :
            is_valid = False
        elif next_number - current_num < 1 or next_number - current_num > 3:
            is_valid = False

        current_num = next_number

    return is_valid

def check_decrease_safe (data):
    is_valid = True
    current_num = data[0]
    for i in range(len(data) - 1):
        next_number = data[i + 1]

        if current_num < next_number :
            is_valid = False
        elif current_num - next_number < 1 or current_num - next_number > 3:
            is_valid = False

        current_num = next_number

    return is_valid


f = open("inputs/2.txt", "r")
levels = f.read().splitlines()
f.close()

correct = 0
correct_with_errors = 0
for level in levels:
    numbers = [int(num) for num in re.findall(r"\d+", level)]

    # only proceed if numbers exists
    if len(numbers) == 0:
        continue

    # Check increase
    if check_increase_safe(numbers):
        correct += 1
        correct_with_errors += 1
        continue
    else:
        # remove a number and try again
        for i in range(len(numbers)):
            copy_numbers = numbers.copy()
            del copy_numbers[i]
            if check_increase_safe(copy_numbers):
                correct_with_errors += 1
                break

    # Check decrease
    if check_decrease_safe(numbers):
        correct += 1
        correct_with_errors += 1
        continue
    else:
        # remove a number and try again
        for i in range(len(numbers)):
            copy_numbers = numbers.copy()
            del copy_numbers[i]
            if check_decrease_safe(copy_numbers):
                correct_with_errors += 1
                break

print(correct)
print(correct_with_errors)