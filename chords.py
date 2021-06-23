from music21 import converter, instrument, note, chord
c1 = chord.Chord(['c', 'e-', 'g', 'b', 'a', 'c2'])
c1.duration.type = 'quarter'
# c1Notes = c1.notes
# print(c1Notes)
print(c1.normalOrder)
print(c1.pitches)
n1 = note.Note("C2")
print(n1.normalOrder())
notes = []
element = chord.Chord(("4", "7"))
if isinstance(element, chord.Chord):
    notes.append('.'.join(str(n) for n in element.normalOrder))

print(notes[0])