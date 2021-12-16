from dataclasses import dataclass
from typing import List, Union

import consts


@dataclass
class Point:
    x: int
    y: int

@dataclass
class Playground:
    walls: List[Point]
    orbs: List[Point]

@dataclass
class Player:
    location: Point
    direction: consts.Direction
    points: int
    stack: List[int]
    script: List[Union[consts.OpCode, int]]

    def turn_left(self) -> None:
        p_dir = self.direction
        if p_dir == consts.Direction.LEFT:
            self.direction = consts.Direction.DOWN
        if p_dir == consts.Direction.DOWN:
            self.direction = consts.Direction.RIGHT
        if p_dir == consts.Direction.RIGHT:
            self.direction = consts.Direction.UP
        if p_dir == consts.Direction.UP:
            self.direction = consts.Direction.LEFT

    def turn_right(self) -> None:
        for _ in range(3):
            self.turn_left()

@dataclass
class Level:
    name: str
    width: int
    height: int
    field: Playground
    player: Player
    tick: int
    script_iteration_limit: int
    stack_limit: int
    tick_limit: int
    error: List[str]
    skip_code: str

    def move_player_forward(self) -> None:
        p_dir = self.player.direction
        if p_dir == consts.Direction.LEFT:
            self.player.location.x -= 1
        if p_dir == consts.Direction.RIGHT:
            self.player.location.x += 1
        if p_dir == consts.Direction.UP:
            self.player.location.y -= 1
        if p_dir == consts.Direction.DOWN:
            self.player.location.y += 1
        self.player.location.x %= self.width
        self.player.location.y %= self.height

