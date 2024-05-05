

from itertools import groupby
 
 
def convert_to_dict(tuple_list):
    # Group the tuples by their first element (the key)
    groups = groupby(tuple_list, key=lambda x: x[0])
 
    # Create an empty dictionary
    dictionary = {}
 
    # Iterate over the groups
    for key, group in groups:
        # Extract the second element of each tuple in the group and add it to the dictionary as the value for the key
        dictionary[key] = [tuple[1] for tuple in group]
 
    return dictionary
 
 
# Test the function
tuple_list = [("akash", 10), ("gaurav", 12), ("anand", 14),
              ("suraj", 20), ("akhil", 25), ("ashish", 30)]
print(convert_to_dict(tuple_list))  # {'akash':