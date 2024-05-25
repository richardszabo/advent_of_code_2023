# Define the lines with potential calibration values
# lines = [
#     "1abc2",
#     "pqr3stu8vwx",
#     "a1b2c3d4e5f",
#     "treb7uchet"
# ]

def read_file(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

# Function to calculate calibration value for a single line
def calculate_calibration_value(line):
    # Extract the first and last digits
    first_digit = next((char for char in line if char.isdigit()), None)
    last_digit = next((char for char in reversed(line) if char.isdigit()), None)

    # Combine them to form a two-digit number
    if first_digit and last_digit:
        return int(first_digit + last_digit)
    else:
        return 0

lines = read_file("data/task1/input.txt")

# Calculate the calibration values for each line and sum them up
total_calibration_value = sum(calculate_calibration_value(line) for line in lines)

# Print the total calibration value
print(f"The total calibration value is: {total_calibration_value}")

# 55386

lines2 = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
]

import re

def extract_digits(input_string):
    # Define a mapping of spelled-out digits to their numeric equivalents
    digit_mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0"
    }

    # Initialize an empty list to store extracted digits
    extracted_digits = []

    # Use regular expression to find all spelled-out digits and numeric digits
    pattern = "|".join(digit_mapping.keys()) + r"|\d"
    matches = re.findall(pattern, input_string, re.IGNORECASE)

    # Iterate through each match
    for match in matches:
        # Check if the match is a spelled-out digit
        if match.lower() in digit_mapping:
            extracted_digits.append(digit_mapping[match.lower()])
        # Check if the match is a numeric digit
        elif match.isdigit():
            extracted_digits.append(match)

    # Join the extracted digits into a single string
    result = "".join(extracted_digits)

    return result

# def extract_digits(line):
#     digits = []
#     for char in line:
#         if char.isdigit():
#             digits.append(char)
#         elif char in "onetwothreefourfivesixseveneightnine":
#             # Map spelled-out digits to their numeric equivalents
#             digit_mapping = {
#                 "one": "1",
#                 "two": "2",
#                 "three": "3",
#                 "four": "4",
#                 "five": "5",
#                 "six": "6",
#                 "seven": "7",
#                 "eight": "8",
#                 "nine": "9"
#             }
#             digits.append(digit_mapping.get(char, ""))  # Empty string if not found
#     return digits

#x = ("".join(extract_digits(line)) for line in lines2)

print(extract_digits("eightwothree"))

def calculate_calibration_value_1b(digits):
    # Extract the first and last digits
    first_digit = digits[0]
    last_digit = digits[-1]

    # Combine them to form a two-digit number
    if first_digit and last_digit:
        return int(first_digit + last_digit)
    else:
        return 0

# Calculate the calibration values for each line and sum them up
#for line in lines:
#    print(line + " " + str(extract_digits(line)) + " " + str(calculate_calibration_value_1b(extract_digits(line))))

total_calibration_value = sum(calculate_calibration_value_1b(extract_digits(line)) for line in lines)

#54807 is wrong

def part2():
    values = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    pairs = []
    for line in lines:
        digits = []
        # start at the first letter and move through it letter by letter.
        # this is the only way i've found to account for overlapping words.
        # an example is "oneight", which only matches "one" when using re.findall.
        for i,c in enumerate(line):
            if line[i].isdigit():
                digits.append(line[i])
            else:
                for k in values.keys():
                    if line[i:].startswith(k):
                        digits.append(values[k])
        pair = int(f"{digits[0]}{digits[-1]}")
        pairs.append(pair)
        copilot_calc = calculate_calibration_value_1b(extract_digits(line))
        if( pair != copilot_calc ):
            print(">>>:" + line + " "+ str(pair) + " " + str(copilot_calc))

    return sum(pairs)

print(part2())

#word = "z7onetwonec"
#print(word + " "+ str(extract_digits(word)))
# def calculate_calibration_value_1b(line):
#     # Extract all digits (both numeric and spelled-out)
#     print(line)
#     return 0
#     digits = [char for char in line if char.isdigit() or char in "onetwothreefourfivesixseveneightnine"]
#
#     # Combine them to form a two-digit number
#     if len(digits) >= 2:
#         return int(digits[0] + digits[-1])
#     else:
#         return 0
#total_calibration_value = sum(calculate_calibration_value_1b(line) for line in lines2)

# Print the total calibration value
print(f"The total calibration value is: {total_calibration_value}")
