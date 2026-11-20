class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = sorted(zip(position, speed), reverse=True)

        fleets = 0
        last_dp, last_s = 0, 1
        for p, s in time:
            dp = target - p
            if fleets == 0 or dp * last_s > last_dp * s:
                fleets += 1
                last_dp, last_s = dp, s

        return fleets