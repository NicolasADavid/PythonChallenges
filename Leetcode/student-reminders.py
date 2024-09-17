
'''
In an incoming class of 100 students (with student IDs 0 through 99), some have registered for classes and some have not. We're given a sorted list of the student IDs who have registered and need to produce a list of people we should contact to remind them. We want this list to be simple and easy to read so we'll format it as follows:

- A single missing student (the students with IDs one larger and smaller) is just the number as a string. So if 30 and 32 have registered, then "31" is in our output.
- If more than one student in a row is missing, we'll show that as a range string. So if 30 and 35 have registered, then "31-34" will appear in our output, since 31, 32, 33, and 34 need to be contacted.

The input will be a sorted array of student ids. The output should be a sorted list of single values (as strings) and range strings as appropriate.
 

EXAMPLE(S)
mustRegister([48, 50]) -> ["0-47", "49", "51-99"]
    

FUNCTION SIGNATURE
function mustRegister(data)
'''


def must_register(nums):

    if not nums:
        return ["0-99"]

    ans = []

    # First number assumed missing
    start = 0

    # Compare number to start
    for num in nums:

        # Start -> number - 1 is missing
        if num > start:

            if num - 1 == start:
                # One missing (start)
                ans.append(str(start))

            else:
                # Range missing (start -> num - 1)
                ans.append(f'{start}-{num-1}')

        # Assume num + 1 is missing
        start = num + 1

    # Last ID(s)
    if start <= 99:
        if start == 99:
            ans.append("99")
        else:
            ans.append(f'{start}-99')

    return ans

print(must_register([]) == ['0-99'])
print(must_register([50]) == ['0-49', '51-99'])
print(must_register([0]) == ['1-99'])
print(must_register([1]) == ['0', '2-99'])
print(must_register([99]) == ['0-98'])
print(must_register([48, 50]) == ['0-47', '49', '51-99'])
print(must_register([47, 50]) == ['0-46', '48-49', '51-99'])
print(must_register([47, 48, 49, 50]) == ['0-46', '51-99'])