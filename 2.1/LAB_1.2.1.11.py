class Interval:
    def __init__(self, hours=0, minutes=0, seconds=0):
        if type(hours) != int:
            raise TypeError("hours should be of type: 'int'")
        if type(minutes) != int:
            raise TypeError("minutes should be of type: 'int'")
        if type(seconds) != int:
            raise TypeError("seconds should be of type: 'int'")

        if hours > 23:
            raise ValueError('hours cannot be larger than 23')
        if minutes > 59 or seconds > 59:
            raise ValueError('minute cannot be larger than 59')
        if seconds > 59:
            raise ValueError('seconds cannot be larger than 59')
        if hours < 0:
            raise ValueError('hours cannot be negative')
        if minutes < 0:
            raise ValueError('minutes cannot be negative')
        if seconds < 0:
            raise ValueError('seconds cannot be negative')

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        hh = str(self.hours).rjust(2, '0')
        mm = str(self.minutes).rjust(2, '0')
        ss = str(self.seconds).rjust(2, '0')
        return f"{hh}:{mm}:{ss}"

    def __add__(self, o):
        s_secs, o_secs = self._to_seconds(intervals=[self, o])

        return self._do_operation(s_secs, o_secs, operation="add")

    def __sub__(self, o):
        s_secs, o_secs = self._to_seconds(intervals=[self, o])

        return self._do_operation(s_secs, o_secs, operation="subtract")

    def __mul__(self, multiplier):
        s_secs = self._to_seconds()

        return self._do_operation(s_secs, multiplier, operation="multiply")

    def _do_operation(self, first, second, operation ="add"):
        if operation == "add":
            t_secs = first + second
        elif operation == "subtract":
            t_secs = first - second
        elif operation == "multiply":
            t_secs = first * second
        else:
            raise ValueError("operator should be 'add', 'subtract', or 'multiply'")

        t_hours, t_minutes, t_seconds = self._get_hh_mm_ss(t_secs)
        return Interval(hours=t_hours, minutes=t_minutes, seconds=t_seconds)

    def _to_seconds(self, intervals = None):
        if intervals is not None:
            res = ()
            for interval in intervals:
                if type(interval) is Interval:
                    res += (interval.hours * 3600 + interval.minutes * 60 + interval.seconds,)
                elif type(interval) is int:
                    res += (interval,)
        else:
            res = self.hours * 3600 + self.minutes * 60 + self.seconds
        return res

    def _get_hh_mm_ss(self, seconds):
        hh = seconds // 3600
        mm = (seconds % 3600) // 60
        ss = (seconds % 3600) % 60

        return hh, mm, ss


test = Interval(hours=2, minutes=22)
test2 = Interval(hours=1, minutes=10)

print(test + test2)
print(test - test2)
print(test * 2)
print(test + 59)
print(test - 30)
