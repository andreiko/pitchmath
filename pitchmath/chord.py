class Chord(object):
    def __init__(self, notes):
        self._notes = notes

    @property
    def notes(self):
        return self._notes

    @property
    def intervals(self):
        result = []

        for i in range(1, len(self._notes)):
            result.append(self._notes[i] - self._notes[0])

        return result

    @property
    def name_base(self):
        intervals = set(self.intervals)
        components = [self._notes[0].to_string()]

        if 3 in intervals:
            components.append('m')

        if 7 in intervals and not intervals & {3, 4, 10, 11}:
            components.append('5')

        return ''.join(components)

    @property
    def name_index(self):
        intervals = set(self.intervals)
        components = []

        if 10 in intervals:
            components.append('7')

        if 11 in intervals:
            components.append('maj7')

        if 6 in intervals:
            components.append('(b5)')

        return ''.join(components)

    @property
    def name(self):
        return ''.join(self.name_base + self.name_index)

    def __str__(self):
        return self.name
