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
    for map2 in list_of_maps:
        # Compare the values in map1 with map2
        is_greater = all(map1[key] > map2.get(key, float('-inf')) for key in map1)
        result.append(is_greater)
    return result

# Example usage:
map1 = {'a': 10, 'b': 20, 'c': 30}
list_of_maps = [{'a': 5, 'b': 15, 'c': 25}, {'a': 12, 'b': 18, 'c': 28}, {'a': 8, 'b': 22, 'c': 32}]

# Call the function
comparison_result = compare_maps(map1, list_of_maps)

print("Comparison result:", comparison_result)
