class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = sorted(zip(position, speed), reverse=True)

        fleets, last_arrival = 0, 0
        for p, s in time:
            t = (target - p) / s
            if fleets == 0 or t > last_arrival:
                fleets += 1
                last_arrival = t

        return fleets