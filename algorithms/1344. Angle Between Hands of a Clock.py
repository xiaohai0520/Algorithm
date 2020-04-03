class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = minutes * 6
        hour_angle = hour%12 * 30 + minutes * 0.5
        res = abs(minute_angle - hour_angle)
        return res if res <= 180 else 360 - res
