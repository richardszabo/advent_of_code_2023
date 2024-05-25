####################################################################################
# version 0
####################################################################################
#This was the answer without code for the below matrix:
#Next to ‘*’: 467, 114, 35, 617
#Next to ‘#’: 633
#Next to ‘+’: 58
#Next to ‘$’: 755, 664
# The solution is wrong: 114 and 58 should not be included and 598 and 592 should.

####################################################################################
# version 1
####################################################################################
matrix = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

symbols = ['*', '#', '+', '$']
numbers = '1234567890'
result = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] in symbols:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == dy == 0:
                        continue
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[i]) and matrix[ni][nj] in numbers:
                        num = ''
                        while 0 <= ni < len(matrix) and 0 <= nj < len(matrix[i]) and matrix[ni][nj] in numbers:
                            num += matrix[ni][nj]
                            ni, nj = ni + dx, nj + dy
                        result.append(int(num))

print("Numbers next to a symbol: ", result)

# The code give the below result.
# It is completely useless, not a single number has been found, even the fact that numbers have multiple digits is neglected.

# Numbers next to a symbol:  [7, 3, 5, 6, 3, 716, 2, 6, 4, 7, 5, 9]

####################################################################################
# version 2
####################################################################################

matrix = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

symbols = ['*', '#', '+', '$']
numbers = '1234567890'
result = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] in symbols:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == dy == 0:
                        continue
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[i]) and matrix[ni][nj] in numbers:
                        num = ''
                        while 0 <= ni < len(matrix) and 0 <= nj < len(matrix[i]) and matrix[ni][nj] in numbers:
                            num += matrix[ni][nj]
                            if dx != 0:
                                ni += dx
                            if dy != 0:
                                nj += dy
                        result.append(int(num))

print("Numbers next to a symbol: ", result)

# After my complaint it correctly formulates the problem but the returned code is almost the same as before and output is the same:

#Numbers next to a symbol:  [7, 3, 5, 6, 3, 716, 2, 6, 4, 7, 5, 9]

####################################################################################
# version 3
####################################################################################

matrix = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

symbols = ['*', '#', '+', '$']
numbers = '1234567890'
result = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] in numbers:
            num = ''
            while j < len(matrix[i]) and matrix[i][j] in numbers:
                num += matrix[i][j]
                j += 1
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == dy == 0:
                        continue
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[i]) and matrix[ni][nj] in symbols:
                        result.append(int(num))
                        break
                else:
                    continue
                break

print("Numbers next to a symbol: ", result)

# This time I gave some examples mentioning 467 and 664 specifically. The list is better but not so much:

#Numbers next to a symbol:  [467, 67, 7, 35, 5, 592, 92, 2, 664, 64, 4]

####################################################################################
# version 4
####################################################################################
matrix = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

symbols = ['*', '#', '+', '$']
numbers = '1234567890'
result = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] in numbers:
            num = ''
            while j < len(matrix[i]) and matrix[i][j] in numbers:
                num += matrix[i][j]
                j += 1
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == dy == 0:
                        continue
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[i]) and matrix[ni][nj] in symbols:
                        result.append(int(num))
                        break
                else:
                    continue
                break

# Filter out the numbers that are not adjacent to any symbol
result = [num for num in result if result.count(num) == 1]

print("Numbers next to a symbol: ", result)

# I explicitly told the numbers that should be excluded.
# The output is still the same:
# Numbers next to a symbol:  [467, 67, 7, 35, 5, 592, 92, 2, 664, 64, 4]

####################################################################################
# version 5
####################################################################################
matrix = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

symbols = ['*', '#', '+', '$']
result = []

# Define all possible directions (horizontal, vertical, diagonal)
directions = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx != 0 or dy != 0]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] in symbols:
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[i]) and matrix[ni][nj].isdigit():
                    num = ''
                    while 0 <= ni < len(matrix) and 0 <= nj < len(matrix[i]) and matrix[ni][nj].isdigit():
                        num += matrix[ni][nj]
                        ni += dx
                        nj += dy
                    result.append(int(num))

print("Numbers next to a symbol: ", result)

# I explicitly told the numbers that should be excluded from his result, like 2,4,5.
# Now I am back to the original result:
# Numbers next to a symbol:  [7, 3, 5, 6, 3, 716, 2, 6, 4, 7, 5, 9]

####################################################################################
# version 6
####################################################################################
import re

matrix = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

# Join all the lines in the matrix into a single string
matrix_str = ''.join(matrix)

# Use a regular expression to find all sequences of digits in the string
numbers = re.findall(r'\d+', matrix_str)

# Convert the numbers to integers and print them
numbers = list(map(int, numbers))

print("All numbers in the matrix: ", numbers)

# I tried something else. Asked for the list numbers without checking symbol adjacency.
# The result is good!
# All numbers in the matrix:  [467, 114, 35, 633, 617, 58, 592, 755, 664, 598]

####################################################################################
# version 7
####################################################################################
matrix = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

# Join all the lines in the matrix into a single string
matrix_str = ''.join(matrix)

# Use a regular expression to find all sequences of digits in the string
numbers = re.findall(r'\d+', matrix_str)

# Convert the numbers to integers
numbers = list(map(int, numbers))

# Define all possible directions (horizontal, vertical, diagonal)
directions = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if dx != 0 or dy != 0]

# List to store numbers adjacent to a symbol
adjacent_numbers = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] in symbols:
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[i]) and matrix[ni][nj].isdigit():
                    num = ''
                    while 0 <= ni < len(matrix) and 0 <= nj < len(matrix[i]) and matrix[ni][nj].isdigit():
                        num += matrix[ni][nj]
                        ni += dx
                        nj += dy
                    adjacent_numbers.append(int(num))

# Filter out the numbers that are not adjacent to any symbol
numbers = [num for num in numbers if num in adjacent_numbers]

print("Numbers next to a symbol: ", numbers)

# My new instructions were:
# This result is good! Now extend the solution with checking whether a number is adjacent to a symbol like  *, $, #,+ and exclude numbers which are not adjacent. For example ,114 and 58 are these numbers.
# Bad, bad:
# Numbers next to a symbol:  []