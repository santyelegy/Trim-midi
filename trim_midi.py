import pretty_midi


def trim(path, time, name):
    midi_data = pretty_midi.PrettyMIDI(path)
    round = 0
    run = True
    while run:
        midi = pretty_midi.PrettyMIDI()
        run = False
        for instrument in midi_data.instruments:
            cuted_instrument = pretty_midi.Instrument(program=instrument.program)
            notes = instrument.notes
            for note in notes:
                if note.start >= round * time and note.end <= (round + 1) * time:
                    note.start = note.start - round * time
                    note.end = note.end - round * time
                    cuted_instrument.notes.append(note)
            if len(cuted_instrument.notes) != 0:
                run = True
            midi.instruments.append(cuted_instrument)
        midi.write(name + '_' + str(round) + ".mid")
        round += 1


if __name__ == "__main__":
    trim("Carol Of The Mando.mid", 6, "Carol Of The Mando")
