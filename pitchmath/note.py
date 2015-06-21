import collections


__all__ = ['Note', 'NoteValue']


class NoteValue(int):
    @classmethod
    def _normalize(cls, value):
        while value < 0:
            value += 12
        while value >= 12:
            value -= 12
        return value

    def __init__(self, x, *args):
        super(NoteValue, self).__init__(x, *args)
        if self._normalize(x) != x:
            raise ValueError("Invalid note value: {}".format(x))

    def __add__(self, other):
        return self._normalize(super(NoteValue, self).__add__(other))

    def __sub__(self, other):
        return self._normalize(super(NoteValue, self).__sub__(other))


class Note(object):
    LETTERS = collections.OrderedDict((
        ('C', NoteValue(0)),
        ('D', NoteValue(2)),
        ('E', NoteValue(4)),
        ('F', NoteValue(5)),
        ('G', NoteValue(7)),
        ('A', NoteValue(9)),
        ('B', NoteValue(11)),
    ))
    LETTERS_REVERSE = {v: l for l, v in LETTERS.items()}

    ALTERATIONS = {
        +1: '#',
        -1: 'b',
    }
    ALTERATIONS_REVERSE = {s: v for v, s in ALTERATIONS.items()}

    def __init__(self, value, use_letter=None, use_alteration=None):
        if not isinstance(value, int):
            raise TypeError
        self._value = NoteValue(value)

        if use_letter and use_letter not in self.LETTERS:
            raise ValueError('Invalid letter: "{}".'.format(use_letter))

        if use_alteration and use_alteration not in self.ALTERATIONS:
            raise ValueError('Invalid alteration: "{}".'.format(use_alteration))

        if use_letter and use_alteration:
            raise ValueError("Only one of use_alteration and use_letter "
                             "may be specified.")

        self._use_letter = use_letter
        self._use_alteration = use_alteration

    @property
    def value(self):
        return self._value

    @property
    def use_alteration(self):
        if self._use_alteration:
            return self._use_alteration
        return +1

    @property
    def letter_value(self):
        if self._use_letter:
            return self.LETTERS[self._use_letter]

        alt = self.use_alteration
        current = self._value
        while True:
            if current in self.LETTERS_REVERSE:
                return current
            current -= alt

    @property
    def letter(self):
        if self._use_letter:
            return self._use_letter
        return self.LETTERS_REVERSE[self.letter_value]

    @property
    def alteration_value(self):
        base = self.letter_value
        choices = [
            int(self._value) - int(base),
            int(self._value) - 12 - int(base),
            int(self._value) + 12 - int(base),
        ]

        choices.sort(key=lambda x: abs(x))

        if self._use_alteration:
            for value in choices:
                if value == 0 or value / abs(value) == self._use_alteration:
                    return value

        return choices[0]

    @property
    def alterations(self):
        value = self.alteration_value
        if value:
            alteration = value / abs(value)
            return self.ALTERATIONS[alteration] * abs(value)
        return ''

    def get_possible_alterations(self):
        return [Note(self.value, use_alteration=alt)
                for alt in self.ALTERATIONS]

    def to_string(self):
        return ''.join((self.letter, self.alterations))

    def __unicode__(self):
        return self.to_string()

    def __str__(self):
        return self.to_string()

    @classmethod
    def from_string(cls, s):
        if not isinstance(s, basestring):
            raise TypeError

        letter = s[:1]
        if letter not in cls.LETTERS:
            raise ValueError('Invalid letter: "{}".'.format(letter))

        letter_value = cls.LETTERS[letter]
        alteration_value = 0

        for c in s[1:]:
            if c in cls.ALTERATIONS_REVERSE:
                alteration_value += cls.ALTERATIONS_REVERSE[c]
            else:
                raise ValueError('Invalid alteration: "{}".'.format(c))

        return cls(value=letter_value + alteration_value, use_letter=letter)

    def __sub__(self, other):
        if not isinstance(other, Note):
            raise ValueError

        interval =  int(self.value) - int(other.value)
        if interval < 0:
            interval += 12

        return interval

    @property
    def next_letter(self):
        letters = self.LETTERS.keys()
        i = letters.index(self.letter)
        if i == len(letters) - 1:
            return letters[0]
        return letters[i + 1]

    @property
    def prev_letter(self):
        letters = self.LETTERS.keys()
        i = letters.index(self.letter)
        if i == 0:
            return letters[-1]
        return letters[i - 1]
