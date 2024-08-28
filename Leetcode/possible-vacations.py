'''
Possible Vacations

We want to take a vacation and are looking at tables of flight schedules and comparing them against our list of desired destinations.

The schedule displays the flight tables as a map of city names as keys and a list of city names reachable via a direct flight as the values. For example:

{
  'Phoenix': [], // dead-end
  'Seattle': ['Phoenix', 'Boston'], // can fly to 'Phoenix' and 'Boston'
  'Boston': ['Phoenix']  // can only fly to 'Phoenix'
}

Given a flight table, a home city, and a list (array) of destinations, return a new map indicating the minimum number of flights needed for each destination. If a destination is not reachable, do not include it in the output.
 

EXAMPLE(S)
possibleVacations(
  {'Phoenix': ['Seattle'], 'Seattle':[]},
  'Phoenix', 
  ['Seattle']
)
returns {'Seattle': 1}

possibleVacations(
  {'Phoenix': [], 'Seattle':[]},
  'Phoenix',
  ['Seattle']
)
returns {}

possibleVacations(
  {'Phoenix': ['Seattle'], 'Seattle':['Boston', 'Phoenix'], 'Boston': ['Phoenix']},
  'Phoenix',
  ['Seattle', 'Boston']
)
returns {'Seattle': 1, 'Boston': 2}


FUNCTION SIGNATURE
function possibleVacations(flightTable, homeCity, destinationList)

APPROACH
- iterate over the destinations and create an object with the city as the key and 0 as the value
- initialize a visited set
- Perform a breadth first search starting from the origin
  - The start: ['Phoenix', 0]
  - [cityName, distance + 1]
  - If the city is in the visited set, don't add it to the queue
  - Add city to the visited set
  - Whenever we come accross a city that is inside of our cities object, then when reset its value to the current distance
- Remove all of the cities from the city object whose value is 0
- return the city object
[]

'''

from collections import deque

def possibleVacations(flightTable, homeCity, destinationList):

    possibleDestinations = {} # city -> flights to get to there from homeCity
    destinationListSet = set(destinationList)
    visited = set()

    queue = deque([(homeCity, 0)])

    while queue:
        city, hops = queue.popleft()

        if city in visited:
            continue
        visited.add(city)

        if city in destinationListSet:
            possibleDestinations[city] = hops

        nextDestinations = flightTable[city]
        for nextDestination in nextDestinations:
            queue.append((nextDestination, hops + 1))
        
    return possibleDestinations



# {'Seattle': 1, 'Boston': 2}
print(
    possibleVacations(
        { 'Phoenix': ['Seattle'], 'Seattle': ['Boston', 'Phoenix'], 'Boston': ['Phoenix'] },
        'Phoenix',
        ['Seattle', 'Boston']
    )
)






'''

function possibleVacations(flightTable, homeCity, destinationList) {
  const destinations = {};

  for (let destination of destinationList) {
    destinations[destination] = 0;
  }

  const visited = new Set();
  const queue = [[homeCity, 0]];

  while (queue.length) {
    const [city, distance] = queue.shift();

    if (visited.has(city)) continue;
    visited.add(city);

    if (city in destinations) destinations[city] = distance + 1;

    if (flightTable[city]) {
      for (let destination of flightTable[city]) {
        queue.push([destination, distance + 1]);
      }
    }
  }

  for (let [key, val] in Object.entries(destinations)) {
    if (val === 0) delete destinations[key];
  }

  return destinations;
}
'''