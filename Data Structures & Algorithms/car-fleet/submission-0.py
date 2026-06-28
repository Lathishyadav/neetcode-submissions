class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))

        cars.sort(reverse=True)

        fleets = 0
        slowest_time = 0

        for pos, spd in cars:
            time = (target - pos) / spd

            if time > slowest_time:
                fleets += 1
                slowest_time = time

        return fleets