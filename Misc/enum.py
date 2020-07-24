from enum import Enum

class State(Enum):
    VISITED = 1
    VISITING = 2
    UNVISITED = 3

# print(repr(State.UNVISITED))
# print(repr(State.VISITING))

# print(State(1))
# print(State.UNVISITED.name)

for state in State:
    print(state)
