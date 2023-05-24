fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

# print(newlist)

# newlist = [expression for item in iterable if condition == True]


newlist = [x for x in range(10)]
newlist = [x for x in range(10) if x < 5]
newlist = [x.upper() for x in fruits]
newlist = ['hello' for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]


matrix = [[i for i in range(5)] for _ in range(6)]
[
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4]
]

letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
letter_int = {x: idx for idx, x in enumerate(letters)}
int_letter = {idx: x for idx, x in enumerate(letters)}
