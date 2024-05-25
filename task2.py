def read_file(filename):
    with open(filename) as file:
        lines = file.read()
        #lines = [line.rstrip() for line in file]
    file.close()
    return lines

def calculate_minimum_cubes(game_data):
    # Initialize dictionaries to store the maximum number of cubes shown for each color
    #max_cubes = {'red': 0, 'green': 0, 'blue': 0}

    # Split the game data into individual games
    games = game_data.split('Game ')[1:]

    # Initialize a dictionary to store the results
    results = {}

    # Process each game
    for game in games:
        # Split the game into its ID and the cube selections
        game_id, selections = game.rstrip('\n').split(': ')
        game_id = int(game_id)  # Convert game ID to an integer

        # Split the selections into individual sets
        sets = selections.split('; ')

        # Initialize a dictionary to store the maximum number of cubes shown in this game for each color
        game_max_cubes = {'red': 0, 'green': 0, 'blue': 0}

        # Process each set of cubes
        for set_of_cubes in sets:
            # Split the set into individual cube counts
            cubes = set_of_cubes.split(', ')

            # Process each cube count
            for cube in cubes:
                # Split the cube count into the number and the color
                count, color = cube.split(' ')
                count = int(count)  # Convert count to an integer

                # Update the maximum number of cubes shown for this color in this game
                game_max_cubes[color] = max(game_max_cubes[color], count)

        # Update the overall maximum number of cubes shown for each color
        #for color in max_cubes:
        #    max_cubes[color] = max(max_cubes[color], game_max_cubes[color])

        # Store the results for this game
        results[game_id] = game_max_cubes

    #return max_cubes, results
    return results

def compare_maps(map1, list_of_maps):
    """
    Compares the values in map1 with the corresponding values in each map from the list_of_maps.
    Returns a list of booleans indicating whether the numbers in map1 are greater than the corresponding numbers
    in each map from the list_of_maps.

    Args:
        map1 (dict): A dictionary with numeric values.
        list_of_maps (list): A list of dictionaries, each containing numeric values.

    Returns:
        list: A list of booleans.
    """
    result = []
    sum_of_fitting_game_ids = 0
    multiplication_sum = 0
    for id,map2 in list_of_maps:
        # Compare the values in map1 with map2
        is_greater_or_equal = all(map1[key] >= map2.get(key, float('-inf')) for key in map1)
        result.append(is_greater_or_equal)
        if( is_greater_or_equal ):
            sum_of_fitting_game_ids = sum_of_fitting_game_ids + id
        multiplication = 1
        for key in map1:
            multiplication *= map2.get(key, 1)
        multiplication_sum += multiplication
    return sum_of_fitting_game_ids,result, multiplication_sum

# Example game data
# game_data = """
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# """

game_data = read_file("data/task2/input.txt")

# Calculate the minimum number of cubes required for each color
#overall_max_cubes,
game_results = calculate_minimum_cubes(game_data)

# Print the results
#print(f"Overall minimum number of cubes required: {overall_max_cubes}")
for game_id, game_max_cubes in game_results.items():
    print(f"Game {game_id}: {game_max_cubes}")

bag = {'red': 12, 'green': 13, 'blue': 14}
sum_of_fitting_game_ids,comparison_result, multiplication_sum = compare_maps(bag, game_results.items())

print("Comparison result:", comparison_result)
print(f"{sum_of_fitting_game_ids=}")

print(f"{multiplication_sum=}")

#a
#1715 too low, > was used instead of >= in compare_maps

#2061

#b
#72596