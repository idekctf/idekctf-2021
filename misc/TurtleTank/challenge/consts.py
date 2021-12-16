import enum


class Direction(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()
    UP = enum.auto()
    DOWN = enum.auto()

class GameState(enum.Enum):
    PLAYING = enum.auto()
    WIN = enum.auto()
    FAILED = enum.auto()

class OpCode(enum.Enum):
    LOAD = enum.auto()
    TICK = enum.auto()
    COPY = enum.auto()
    DEL = enum.auto()

    RIGHT = enum.auto()
    LEFT = enum.auto()

    IF = enum.auto()
    JMP = enum.auto()
    SKP = enum.auto()

    ADD = enum.auto()
    SUB = enum.auto()
    MOD = enum.auto()
