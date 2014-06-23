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

import abc
import itertools


class Receiver:
    """A car stereo receiver.

    Methods are buttons on the receiver panel.

    This is the Context in the State pattern.
    """

    def __init__(self):
        self.source = FMRadioSource()

    def change_source(self):
        if isinstance(self.source, FMRadioSource):
            self.source = AMRadioSource()
        elif isinstance(self.source, AMRadioSource):
            self.source = CDSource()
        else:
            self.source = FMRadioSource()

    def skip(self):
        self.source.skip()

    def pause(self):
        self.source.pause()

    def play(self):
        self.source.play()

    def __repr__(self):
        return '<Receiver source: {}>'.format(self.source)


class Source(metaclass=abc.ABCMeta):

    def __init__(self, receiver):
        self.receiver = receiver
        self.mode = 'play'

    @abc.abstractmethod
    def skip(self):
        """Skip to next station or track"""

    @abc.abstractmethod
    def pause(self):
        """Mute radio or pause playback"""

    @abc.abstractmethod
    def play(self):
        """Unmute radio or start/resume playback"""


class RadioSource(Source):
    """Generic radio source"""

    def __init__(self):
        self.scanner = itertools.cycle(self.stations)
        self.skip()
        self.play()

    def __str__(self):
        fmt = '{} {} ({})'
        return fmt.format(self.band, self.playing, self.mode)

    def skip(self):
        self.playing = next(self.scanner)

    def pause(self):
        self.mode = 'mute'

    def play(self):
        self.mode = 'play'


class FMRadioSource(RadioSource):
    band = 'FM'
    stations = [89.1, 90.5, 96.9, 100.9, 103.3]


class AMRadioSource(RadioSource):
    band = 'AM'
    stations = [620, 780, 840, 1040, 1200]


class CDSource(Source):
    tracks = ["And I Love Her", "Any Time at All", "Can't Buy Me Love",
              "A Hard Day's Night", "I Should Have Known Better"]

    def __init__(self):
        self.player = itertools.cycle(enumerate(self.tracks, 1))
        self.skip()
        self.play()

    def __str__(self):
        fmt = 'CD track #{0[0]}:"{0[1]}" ({1})'
        return fmt.format(self.playing, self.mode)

    def skip(self):
        self.playing = next(self.player)

    def pause(self):
        self.mode = 'pause'

    def play(self):
        self.mode = 'play'
