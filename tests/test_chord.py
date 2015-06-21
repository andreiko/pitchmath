from pitchmath import Note, Chord, major_scale


def test_scale_chords():
    chords = major_scale.get_chords_for_base(Note.from_string('C'), (1, 3,
                                                                     5, 7))

    assert map(str, chords) == ['Cmaj7', 'Dm7', 'Em7', 'Fmaj7', 'G7', 'Am7',
                                'Bm7(b5)']

def test_5():
    assert Chord(map(Note.from_string, ['C', 'G'])).name == 'C5'
    assert Chord(map(Note.from_string, ['B', 'F'])).name == 'B(b5)'


def test_major():
    assert Chord(map(Note.from_string, ['C', 'E', 'G'])).name == 'C'
    assert Chord(map(Note.from_string, ['Bb', 'D', 'F'])).name == 'Bb'


def test_minor():
    assert Chord(map(Note.from_string, ['A', 'C', 'E'])).name == 'Am'
    assert Chord(map(Note.from_string, ['C#', 'E', 'G#'])).name == 'C#m'


def test_7():
    assert Chord(map(Note.from_string, ['C', 'E', 'G', 'B'])).name == 'Cmaj7'
    assert Chord(map(Note.from_string, ['B', 'D', 'F', 'A'])).name == 'Bm7(b5)'
    assert Chord(map(Note.from_string, ['G', 'B', 'D', 'F'])).name == 'G7'
