from typing import List
import heapq

class Flight():

    def __init__(self, departure: int, landing: int) -> None:
        self.departure = departure
        self.landing = landing

class Solution():

    def maxFlightsInAir(self, flights: List["Flight"]) -> int:

        # TODO: Sort list in place? Don't use heap?

        # Min heap with tuples (departure, tiebreaker, flight)
        toDepartFlights = []
        tb = 0

        for flight in flights:
            tb += 1
            flightTuple = (flight.departure, tb, flight)
            heapq.heappush(toDepartFlights, flightTuple)

        best = 0

        # Min heap with tuples (landing, tiebreaker, flight)
        planesFlying = []

        # Fly and land planes until all planes have taken off
        while toDepartFlights:

            nextFlightTuple = heapq.heappop(toDepartFlights)
            nextDeparture = nextFlightTuple[0]

            # Take off next flight
            tb += 1
            nextDepartureTuple = (nextFlightTuple[2].landing, tb, nextFlightTuple[2])
            heapq.heappush(planesFlying, nextDepartureTuple)

            # Land flights
            while planesFlying and planesFlying[0][0] < nextDeparture:
                heapq.heappop(planesFlying)
            
            # Update best
            best = max(best, len(planesFlying))

        return best

if __name__ == "__main__":
    f1 = Flight(4, 8)
    f2 = Flight(2, 5)
    f3 = Flight(17, 20)
    f4 = Flight(10, 21)
    f5 = Flight(9, 18)

    flights = [f1, f2, f3, f4, f5]

    print(Solution().maxFlightsInAir(flights))

