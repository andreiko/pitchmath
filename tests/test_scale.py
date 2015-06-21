from pitchmath import major_scale, minor_scale, Note


def test_major_scales():
    c_major_notes = major_scale.get_notes_for_base(Note.from_string('C'))
    assert map(str, c_major_notes) == ['C', 'D', 'E', 'F', 'G', 'A', 'B']

    csharp_major_notes = major_scale.get_notes_for_base(Note.from_string('C#'))
    assert map(str, csharp_major_notes) == ['C#', 'D#', 'E#', 'F#', 'G#',
                                            'A#', 'B#']

    dsharp_major_notes = major_scale.get_notes_for_base(Note.from_string('D#'))
    assert map(str, dsharp_major_notes) == ['Eb', 'F', 'G', 'Ab', 'Bb',
                                            'C', 'D']


def test_minor_scales():
    a_minor_notes = minor_scale.get_notes_for_base(Note.from_string('A'))
    assert map(str, a_minor_notes) == ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    g_minor_notes = minor_scale.get_notes_for_base(Note.from_string('G'))
    assert map(str, g_minor_notes) == ['G', 'A', 'Bb', 'C', 'D', 'Eb', 'F']

    dflat_minor_notes = minor_scale.get_notes_for_base(Note.from_string('Db'))
    assert map(str, dflat_minor_notes) == ['C#', 'D#', 'E', 'F#', 'G#',
                                           'A', 'B']
