"""
State pattern example, based on Python and Ruby examples at:
http://en.wikibooks.org/wiki/Computer_Science_Design_Patterns/State

Description
-----------

"Objects often need to change behavior when they are in certain states.
Define an interface comprising all methods that change behavior;
interface implementations define behavior for each state."   (From:
Holub on Patterns, p. 392)

Participants
------------

Context (Receiver)
    Defines the interface of interest to clients. Its current state is
    given by an instance of a ConcreteState sublass.

State (Source)
    Defines an interface for encapsulating all the behavior that
    changes when the the state of the Context changes

ConcreteState subclasses (FMRadioSource, AMRadioSource, CDSource...)
    Each subclass implements the State interface according to the
    behavior specific to each state of the Context.

"""

import itertools


class Receiver:
    """A car stereo receiver.

    Methods are buttons on the receiver panel.

    This is the Context in the State pattern.
    """

    def __init__(self):
        self.sources = itertools.cycle([FMRadioSource(), CDSource()])
        self.change_source()

    def change_source(self):
        self.source = next(self.sources)

    def skip(self):
        """Skip to next station or track"""
        self.source.skip()

    def pause(self):
        """Mute radio or pause playback"""
        self.source.pause()

    def play(self):
        """Unmute radio or start/resume playback"""
        self.source.play()

    def __repr__(self):
        return '<Receiver source: {}>'.format(self.source)


class FMRadioSource:
    band = 'FM'
    stations = [89.1, 90.5, 96.9, 100.9, 103.3]

    def __init__(self):
        self.scanner = itertools.cycle(self.stations)
        self.skip()
        self.play()

    def __str__(self):
        fmt = '{} {}{}'
        mute_display = ' (muted)' if self.muted else ''
        return fmt.format(self.band, self.tuned, mute_display)

    def skip(self):
        self.tuned = next(self.scanner)

    def pause(self):
        self.muted = True

    def play(self):
        self.muted = False


class CDSource:
    tracks = ["And I Love Her", "Any Time at All", "Can't Buy Me Love",
              "A Hard Day's Night", "I Should Have Known Better"]

    def __init__(self):
        self.player = itertools.cycle(enumerate(self.tracks, 1))
        self.skip()
        self.play()

    def __str__(self):
        fmt = 'CD track #{0[0]}:"{0[1]}" ({1})'
        return fmt.format(self.track, self.mode)

    def skip(self):
        self.track = next(self.player)

    def pause(self):
        self.mode = 'paused'

    def play(self):
        self.mode = 'playing'
