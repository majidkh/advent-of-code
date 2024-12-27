import re
import num2words
f = open('inputs/1.txt')
lines = f.read().splitlines()
f.close()

def calculate_1():
    total = 0
    for l in lines:
        numbers = re.findall(r'(\d)', l)
        if len(numbers) >= 1:
            total += int(numbers[0] + numbers[-1])
    return total

def calculate_2():

    # Build a 2d-array of numbers and spellings
    numbers = []
    for i in range(0,10):
        numbers.append([i , str(i)])
    for i in range(100):
        numbers.append([i , num2words.num2words(i).replace('-', '')])

    total = 0
    for line in lines:

        left_index = float("inf")
        right_value = left_value = 0
        right_index = -1

        for value,number in numbers:

            # Find the first number from the left
            left = line.find( str(number))
            if left < left_index and left != -1:
                left_index = left
                left_value = value

            # Find the first number from the right
            right = line.rfind( str(number))
            if right != -1:
                right += len(str(number)) - 1
                if right > right_index:
                    right_index = right
                    right_value = value

        # Glue them together
        number = str(left_value)[0] + str(right_value)[-1]

        # Sum up first and last digits
        total  += int(number[0] + number[-1])
    return total

print("part 1:", calculate_1())
print("part 2:", calculate_2())