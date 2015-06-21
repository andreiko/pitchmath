from .note import Note
from .chord import Chord


__all__ = ['Scale', 'major_scale', 'minor_scale', 'BASIC_SCALES']


class Scale(object):
    def __init__(self, name, intervals):
        self._name = name
        self._intervals = intervals

    @property
    def name(self):
        return self._name

    def _get_notes_for_base(self, base):
        notes = [base]
        prev = base
        for interval in self._intervals:
            prev = Note(prev.value + interval, use_letter=prev.next_letter)
            notes.append(prev)
        return notes

    def get_notes_for_base(self, base):
        if base.alteration_value:
            bases = base.get_possible_alterations()
        else:
            bases = [base]

        results = [self._get_notes_for_base(b) for b in bases]

        results.sort(key=lambda notes: max([abs(n.alteration_value)
                                            for n in notes]))
        return results[0]

    def get_chords_for_base(self, note, degrees=(1, 3, 5)):
        scales = self.get_notes_for_base(note) * 2
        chords = []
        for i in range(1 + len(self._intervals)):
            chords.append(Chord([scales[i - 1 + d] for d in degrees]))
        return chords


major_scale = Scale('major', (2, 2, 1, 2, 2, 2))
minor_scale = Scale('minor', (2, 1, 2, 2, 1, 2))

BASIC_SCALES = [major_scale, minor_scale]
