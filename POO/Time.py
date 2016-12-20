class Time:
    """class containing durations in the form of
    a number of minutes and seconds """

    def __init__(self, min=0, sec=0):
        """class constructor"""
        self.min = min
        self.sec = sec
        self.tmp = 5

    def __str__(self):
        """printing of objects"""
        return "{0:02}:{1:02}".format(self.min, self.sec)

    def __add__(self, other):
        """you'll add number of seconds"""
        new_duration = Time()

        new_duration.min = self.min
        new_duration.sec = self.sec

        new_duration.sec += other

        if new_duration.sec >= 60:
            new_duration.min += new_duration.sec // 60
            new_duration.sec = (new_duration.sec % 60)

        return new_duration

    def __eq__(self, other):
        """if its equal or not to other object Time"""
        return self.min == other.min and self.sec == other.sec

    def __gt__(self, other):
        sec1 = self.sec + (self.min*60)
        sec2 = other.sec + (other.min*60)
        return sec1 > sec2

    def __getstate__(self):
        """Return the attribute dictionary to serialise"""
        dict_attr = dict(self.__dict__)
        dict_attr["tmp"] = 0
        return dict_attr

    def __setstate__(self, state):
        """Method called when we deserialise the object"""
        state["tmp"] = 0
        self.__dict__ = state

t1 = Time(5, 8)
print(t1.__setstate__(t1.__dict__))
t2 = t1 + 124

print( t1 < t2 )