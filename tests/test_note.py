import pytest

from pitchmath import NoteValue, Note


def test_notevalue():
    assert NoteValue(4) + 7 == 11
    assert NoteValue(2) - 3 == 11
    assert NoteValue(2) - 3 == 11
    assert NoteValue(8) + 15 == 11
    assert NoteValue(11) - 36 == 11

    with pytest.raises(ValueError):
        NoteValue(-1)

    with pytest.raises(ValueError):
        NoteValue(12)


def test_from_string():
    assert Note.from_string('G').value == 7
    assert Note.from_string('Cb').value == 11
    assert Note.from_string('B#').value == 0
    assert Note.from_string('E###').value == 7
    assert Note.from_string('Gbbb').value == 4

    with pytest.raises(ValueError):
        Note.from_string('H#')

    with pytest.raises(ValueError):
        Note.from_string('Cb-')


def test_letter():
    assert Note.from_string('G#b#b#').letter == 'G'

    assert Note(11).letter == 'B'

    assert Note(1).letter == 'C'
    assert Note(1, use_alteration=+1).letter == 'C'
    assert Note(1, use_alteration=-1).letter == 'D'


def test_alterations():
    assert Note(5).alterations == ''
    assert Note(5, use_letter='F').alterations == ''
    assert Note(5, use_letter='E').alterations == '#'

    assert Note(7, use_alteration=+1).alterations == ''
    assert Note(7, use_alteration=-1).alterations == ''

    assert Note(11, use_letter='C').alterations == 'b'
    assert Note(0, use_letter='B').alterations == '#'


def test_to_string():
    assert Note.from_string('G##b').to_string() == 'G#'
    assert Note(5, use_letter='G').to_string() == 'Gbb'


def test_sibling_letters():
    assert Note.from_string('Fb').next_letter == 'G'
    assert Note.from_string('Ebb').prev_letter == 'D'

    assert Note.from_string('B').next_letter == 'C'
    assert Note.from_string('Cb').prev_letter == 'B'


def test_substraction():
    assert Note.from_string('E') - Note.from_string('C') == 4
    assert Note.from_string('C') - Note.from_string('B') == 1
    assert Note.from_string('E') - Note.from_string('F') == 11